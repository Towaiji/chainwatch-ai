from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("Starting up PriceAgent...")
    yield
    # Shutdown logic
    print("Shutting down PriceAgent...")

# Pass the lifespan function to the FastAPI constructor.
app = FastAPI(lifespan=lifespan)

@app.get("/price")
async def get_price():
    """
    Endpoint to get mock price data.
    """
    return {"BTC": "50000", "ETH": "4000"}

if __name__ == "__main__":
    # Run the FastAPI app with uvicorn on port 8000
    uvicorn.run("price_agent:app", host="0.0.0.0", port=8000, reload=True)
