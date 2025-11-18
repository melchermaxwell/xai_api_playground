import asyncio
import os
from dotenv import load_dotenv
from xai_sdk import AsyncClient
from xai_sdk.chat import Response, user

load_dotenv()

async def main():
    client = AsyncClient(
        api_key=os.getenv("XAI_API_KEY"),
        timeout=3600, # Override default timeout with longer timeout for reasoning models
    )

    model = "grok-4"
    requests = [
        "What is the longest runway in the USA?",
        "What is the shortest runway in the USA?",
        "What is the longest runway in the world?",
        "What is the shortest runway in the world?",
    ]
    # Define a semaphore to limit concurrent requests (e.g., max 2 concurrent requests at a time)
    max_in_flight_requests = 2
    semaphore = asyncio.Semaphore(max_in_flight_requests)

    async def process_request(request) -> Response:
        async with semaphore:
            print(f"Processing request: {request}")
            chat = client.chat.create(model=model, max_tokens=100)
            chat.append(user(request))
            return await chat.sample()

    tasks = []
    for request in requests:
        tasks.append(process_request(request))

    responses = await asyncio.gather(*tasks)
    for i, response in enumerate(responses):
        print(f"Total tokens used for response {i}: {response.usage.total_tokens}")

if __name__ == "__main__":
    asyncio.run(main())
