import os
from datetime import timedelta
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system

load_dotenv()

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=60, # 1 minute
)

chat = client.chat.create(
    model="grok-4",
    messages=[system("You are Zaphod Beeblebrox.")]
)
chat.append(user("126/3=?"))

# Poll the result every 10 seconds for a maximum of 10 minutes

response = chat.defer(
    timeout=timedelta(minutes=10), interval=timedelta(seconds=10)
)

# Print the result when it is ready

print(response.content)