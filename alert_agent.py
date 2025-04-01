from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uagents import Agent, Context, Bureau

# Define the request schema
class QueryRequest(BaseModel):
    query: str

# Create the FastAPI app
app = FastAPI()

# Define the agent address
ALERT_AGENT_ADDR = "agent1qfhsk62u4cdc5mh6xglg4kwyu8ddqgpjsckvqjwfgvp0qcqyvqz4xckqxnt"

# Create the Agent
agent = Agent(name="AlertAgent", seed="alertagent")

# Define the startup event
@app.on_event("startup")
async def startup():
    # Start the agent
    agent.run()
    print("📡 AlertAgent is online!")

# Endpoint to handle the query
@app.post("/submit")
async def submit_query(query: QueryRequest):
    # Example: Here you need to handle the logic for setting alerts
    if "alert" in query.query.lower():
        # Example logic for alerts
        return {"alert": "Alert set for Bitcoin price drop."}  # Replace with actual logic for alert setting
    else:
        raise HTTPException(status_code=400, detail="Unknown query type")

# Add the agent to the bureau
bureau = Bureau()
bureau.add(agent)

# Run the Bureau on port 8003
if __name__ == "__main__":
    bureau.run()  # This will start the agent on port 8000 internally (no need to pass host and port)
