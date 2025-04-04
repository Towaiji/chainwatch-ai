from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import os
import requests

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up NewsAgent with NewsAPI data...")
    yield
    print("Shutting down NewsAgent...")

app = FastAPI(lifespan=lifespan)

@app.get("/news")
async def get_news():
    """
    Fetches top crypto-related headlines from NewsAPI.
    """
    if not NEWS_API_KEY:
        return {"error": "NEWS_API_KEY not set. Please set your environment variable."}
    try:
        url = f"https://newsapi.org/v2/everything?q=crypto&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        headlines = [article["title"] for article in articles[:3]]
        return {"headlines": headlines}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("news_agent:app", host="0.0.0.0", port=8001, reload=True)
