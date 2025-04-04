import requests

def test_price_agent():
    try:
        response = requests.get("http://localhost:8000/price")
        print("PriceAgent response:", response.json())
    except Exception as e:
        print("Error sending message to PriceAgent:", e)

def test_news_agent():
    try:
        response = requests.get("http://localhost:8001/news")
        print("NewsAgent response:", response.json())
    except Exception as e:
        print("Error sending message to NewsAgent:", e)

def test_alert_agent():
    try:
        response = requests.get("http://localhost:8002/alert")
        print("AlertAgent response:", response.json())
    except Exception as e:
        print("Error sending message to AlertAgent:", e)

def test_assistant_agent():
    try:
        response = requests.get("http://localhost:8003/assistant", params={"message": "What is the price of BTC and crypto news?"})
        print("AssistantAgent response:", response.json())
    except Exception as e:
        print("Error sending message to AssistantAgent:", e)

if __name__ == "__main__":
    test_price_agent()
    test_news_agent()
    test_alert_agent()
    test_assistant_agent()