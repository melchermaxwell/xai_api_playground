import os
from datetime import timedelta
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system

load_dotenv()

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    management_api_key=os.getenv("XAI_MANAGEMENT_API_KEY"),
    timeout=60, # 1 minute
)

#Print all collections
# collections = client.collections.list()
# print(collections)

response = client.collections.search(
    query="What is the never exceed speeds for the planes in the collection?",
    collection_ids=["collection_d5950948-3707-480d-8bdf-8d61674b44eb"],
)
print(response)