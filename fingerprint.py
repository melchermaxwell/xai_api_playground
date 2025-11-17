import os
import json
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system, tool, tool_result
from pydantic import BaseModel, Field
from typing import Literal
import random

load_dotenv()

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=60, # 1 minute
)

chat = client.chat.create(
    model="grok-4-fast",
)

chat.append(user("What is the best superhero movie?"))
chat.append(system("You are a helpful assistant that can answer questions and help with tasks."))
response = chat.sample()


#print(response)
print("System fingerprint: ", response.system_fingerprint)