import httpx

AGENTS = {
    "PriceAgent": "http://127.0.0.1:8001",
    "NewsAgent": "http://127.0.0.1:8002",
    "AlertAgent": "http://127.0.0.1:8003",
    "AssistantAgent": "http://127.0.0.1:8004"
}

# Send a test message to all agents
async def send_message(agent_name, query):
    url = f"{AGENTS[agent_name]}/submit"
    data = {"query": query}
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data)
            if response.status_code == 200:
                print(f"Response from {agent_name}: {response.json()}")
            else:
                print(f"❌ Response from {agent_name}: {response.status_code} - {response.text}")
                if response.status_code == 500:
                    print(f"Error Details: {response.json()}")
    except Exception as e:
        print(f"Error sending message to {agent_name}: {e}")

# Example test
import asyncio
asyncio.run(send_message("PriceAgent", "What is the price of Bitcoin?"))
