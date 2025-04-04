from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import requests

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up AssistantAgent...")
    yield
    print("Shutting down AssistantAgent...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/assistant")
async def get_assistant(message: str = Query(..., description="Message for the assistant")):
    """
    Processes the query and aggregates responses from PriceAgent and NewsAgent.
    """
    response_data = {}
    lower_message = message.lower()

    if "price" in lower_message or "btc" in lower_message:
        try:
            price_resp = requests.get("http://localhost:8000/price")
            response_data["price"] = price_resp.json()
        except Exception as e:
            response_data["price_error"] = str(e)
    
    if "news" in lower_message or "crypto" in lower_message:
        try:
            news_resp = requests.get("http://localhost:8001/news")
            response_data["news"] = news_resp.json()
        except Exception as e:
            response_data["news_error"] = str(e)
    
    if "alert" in lower_message:
        try:
            alert_resp = requests.get("http://localhost:8002/alert")
            response_data["alert"] = alert_resp.json()
        except Exception as e:
            response_data["alert_error"] = str(e)
    
    if not response_data:
        response_data["response"] = f"Assistant received your message: '{message}'"
    
    return {"response": response_data}

if __name__ == "__main__":
    uvicorn.run("assistant_agent:app", host="0.0.0.0", port=8003, reload=True)
