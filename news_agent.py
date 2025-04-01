from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up NewsAgent...")
    # Perform any startup tasks here (e.g., initializing API clients)
    yield
    # Perform any cleanup tasks here
    print("Shutting down NewsAgent...")

# Create the FastAPI app with the lifespan handler
app = FastAPI(lifespan=lifespan)

@app.get("/news")
async def get_news():
    """
    Endpoint to get top crypto news headlines.
    """
    # Example mock news headlines
    return {
        "headlines": [
            "Crypto Market Reaches New Highs",
            "New Regulations Impact Crypto Trading",
            "Major Partnership Announced in Blockchain Space"
        ]
    }

if __name__ == "__main__":
    # Run the FastAPI app with uvicorn on port 8001
    uvicorn.run("news_agent:app", host="0.0.0.0", port=8001, reload=True)
