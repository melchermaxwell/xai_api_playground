import os
from dotenv import load_dotenv

from xai_sdk import Client
from xai_sdk.chat import user, system

load_dotenv()

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=90600, # Override default timeout for longer timeout for reasoning models
)

chat = client.chat.create(model="grok-4-fast")
chat.append(system("You are an airport handler who helps pilots."))
chat.append(user("What is the longest runway in the USA? Simply return the airport identifier in JSON format like {airport_identifier: 'KLAX'}"))

response = chat.sample()
print(response.content)