from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uagents import Agent, Context, Bureau

# Define the request schema
class QueryRequest(BaseModel):
    query: str

# Create the FastAPI app
app = FastAPI()

# Define the agent address
ASSISTANT_AGENT_ADDR = "agent1qdx3tckuw3krnl6vjj2s5q478ehrpq5klwarmzzms2729x85fmcpx7ezdgm"

# Create the Agent
agent = Agent(name="AssistantAgent", seed="assistantagent")

# Define the startup event
@app.on_event("startup")
async def startup():
    # Start the agent
    agent.run()
    print("🤖 AssistantAgent is ready!")

# Endpoint to handle the query
@app.post("/submit")
async def submit_query(query: QueryRequest):
    # Example: Here you need to handle the logic for tasks and other assistant functionalities
    if "tasks" in query.query.lower():
        # Example logic for tasks
        return {"tasks": "Task 1: Complete the project."}  # Replace with actual logic for tasks
    else:
        raise HTTPException(status_code=400, detail="Unknown query type")

# Add the agent to the bureau
bureau = Bureau()
bureau.add(agent)

# Run the Bureau on port 8004
if __name__ == "__main__":
    bureau.run()  # This will start the agent on port 8000 internally (no need to pass host and port)
