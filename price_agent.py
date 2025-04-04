from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import requests

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up PriceAgent with CoinGecko data...")
    yield
    print("Shutting down PriceAgent...")

app = FastAPI(lifespan=lifespan)

@app.get("/price")
async def get_price():
    """
    Fetches the current BTC price (USD) from CoinGecko.
    """
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        btc_price = data["bitcoin"]["usd"]
        return {"BTC": btc_price}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("price_agent:app", host="0.0.0.0", port=8000, reload=True)
