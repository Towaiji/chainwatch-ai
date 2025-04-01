from fastapi import FastAPI, Query
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up AssistantAgent...")
    # Insert any startup tasks here
    yield
    # Insert any shutdown/cleanup tasks here
    print("Shutting down AssistantAgent...")

app = FastAPI(lifespan=lifespan)

@app.get("/assistant")
async def get_assistant(message: str = Query("Hello", description="Message for the assistant")):
    """
    Endpoint to interact with the Assistant Agent.
    Returns a simple echo response for demonstration.
    """
    return {"response": f"Assistant received your message: '{message}'"}

if __name__ == "__main__":
    # Run the FastAPI app with uvicorn on port 8003
    uvicorn.run("assistant_agent:app", host="0.0.0.0", port=8003, reload=True)
