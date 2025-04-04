from fastapi import FastAPI, Query
from contextlib import asynccontextmanager
import uvicorn
import requests

# Map common coin symbols to CoinGecko coin IDs.
coin_mapping = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "ltc": "litecoin",
    "xrp": "ripple",
    "bch": "bitcoin-cash",
    "ada": "cardano",
    "dot": "polkadot",
    "sol": "solana",
    "doge": "dogecoin"
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up PriceAgent with CoinGecko data...")
    yield
    print("Shutting down PriceAgent...")

app = FastAPI(lifespan=lifespan)

@app.get("/price")
async def get_price(coin: str = Query("btc", description="The symbol of the cryptocurrency (e.g. btc, eth, ltc)")):
    """
    Fetches the current coin price (USD) from CoinGecko.
    """
    coin_lower = coin.lower()
    # Use mapping if available, else assume coin_lower is already the correct ID.
    coin_id = coin_mapping.get(coin_lower, coin_lower)
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        if coin_id in data:
            price = data[coin_id]["usd"]
            return { coin.upper(): price }
        else:
            return {"error": f"Price for {coin} not found."}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("price_agent:app", host="0.0.0.0", port=8000, reload=True)
