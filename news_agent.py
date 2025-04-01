from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uagents import Agent, Context, Bureau

# Define the request schema
class QueryRequest(BaseModel):
    query: str

# Create the FastAPI app
app = FastAPI()

# Define the agent address
NEWS_AGENT_ADDR = "agent1qdy6ux98w630pj3d6neypwym00fzsxj43vavxcygqgklw9acsjae62sm6k4"

# Create the Agent
agent = Agent(name="NewsAgent", seed="newsagent")

# Define the startup event
@app.on_event("startup")
async def startup():
    # Start the agent
    agent.run()
    print("📰 NewsAgent is live!")

# Endpoint to handle the query
@app.post("/submit")
async def submit_query(query: QueryRequest):
    # Example: Here you need to handle the logic for news
    if "news" in query.query.lower():
        # Example logic for returning news
        return {"news": "Crypto news goes here"}  # Replace with actual logic for news retrieval
    else:
        raise HTTPException(status_code=400, detail="Unknown query type")

# Add the agent to the bureau
bureau = Bureau()
bureau.add(agent)

# Run the Bureau on port 8002
if __name__ == "__main__":
    bureau.run()  # This will start the agent on port 8000 internally (no need to pass host and port)
