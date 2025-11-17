import os
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system

load_dotenv()

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=60, # 1 minute
)

response = client.image.sample(
    model="grok-2-image",
    prompt="A girl finishing marathon on mars",
    #image_format="url"
    image_format="base64"
)
print(response.image)
#print(response.url)