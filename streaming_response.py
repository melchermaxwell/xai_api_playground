import os
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system

load_dotenv()

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=60, # 1 minute
)

chat = client.chat.create(model="grok-4")
chat.append(
    system("You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."),
)
chat.append(
    user("What is the best comedy show of all time?")
)

for response, chunk in chat.stream():
    print(chunk.content, end="", flush=True) # Each chunk's content
    print(response.content, end="", flush=True) # The response object auto-accumulates the chunks

print(response.content) # The full response
