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


class RandomNumberRequest(BaseModel):
    minimum: int = Field(description="The minimum number", default=1)
    maximum: int = Field(description="The maximum number", default=100)

def get_random_number(request: RandomNumberRequest):
    return {
        "number": random.randint(request.minimum, request.maximum),
    }


# Generate the JSON schema from the Pydantic models
get_random_number_schema = RandomNumberRequest.model_json_schema()

# Definition of parameters with Pydantic JSON schema

tool_definitions = [
    tool(
        name="get_random_number",
        description="Get a random number between a minimum and maximum value",
        parameters=get_random_number_schema,
    )
]

tools_map = {
    "get_random_number": get_random_number,
}

chat = client.chat.create(
    model="grok-4",
    tools=tool_definitions,
    tool_choice="auto",
)
chat.append(user("What is a random number between 200 and 300?"))
response = chat.sample()
# You can inspect the response tool calls which contains a tool call
print(response.tool_calls)

# Append assistant message including tool calls to messages
chat.append(response)
# Check if there is any tool calls in response body
# You can also wrap this in a function to make the code cleaner
if response.tool_calls:
    for tool_call in response.tool_calls:
        # Get the tool function name and arguments Grok wants to call
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        # Call one of the tool function defined earlier with arguments
        if function_name == "get_random_number":
            request = RandomNumberRequest(**function_args)
            result = tools_map[function_name](request)
        else:
            result = tools_map[function_name](**function_args)
        # Append the result from tool function call to the chat message history
        chat.append(tool_result(json.dumps(result)))


response = chat.sample()
print(response.content)