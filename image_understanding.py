import os
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system, image

load_dotenv()

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=90, # 1 minute
)

image_url = "https://flyingtexas.org/N1836TMountains.png"
chat = client.chat.create(model="grok-4")
chat.append(
    user(
        "What type of plane is this?",
        image(image_url=image_url, detail="high"),
    )
)
response = chat.sample()
print(response)