import os
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system
from pydantic import BaseModel, Field

load_dotenv()

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=60, # 1 minute
)

class Address(BaseModel):
    street: str = Field(description="Street address")
    city: str = Field(description="City")
    postal_code: str = Field(description="Postal/ZIP code")
    country: str = Field(description="Country")


chat = client.chat.create(model="grok-4-fast")
chat.append(system("Given a raw address, carefully analyze the text and extract the address data into JSON format."))
chat.append(user("My address is 123 Main St, Anytown, USA, 12345"))

response, address = chat.parse(Address)
assert isinstance(address, Address)

print(address.street)
print(address.city)
print(address.postal_code)
print(address.country)
print(response.content)