from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up AlertAgent...")
    # Initialize any resources needed for alerts
    yield
    # Cleanup resources when shutting down
    print("Shutting down AlertAgent...")

# Create the FastAPI app with the lifespan handler
app = FastAPI(lifespan=lifespan)

@app.get("/alert")
async def get_alert():
    """
    Endpoint to get a simulated price alert.
    """
    # In a real scenario, this could be dynamic based on conditions.
    return {
        "alert": "Price threshold reached: BTC has dropped below your set threshold."
    }

if __name__ == "__main__":
    # Run the FastAPI app with uvicorn on port 8002
    uvicorn.run("alert_agent:app", host="0.0.0.0", port=8002, reload=True)
