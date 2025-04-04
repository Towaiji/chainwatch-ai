# ChainWatch AI

![tag : innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)

ChainWatch AI is a modular suite of specialized AI agents designed for real-time crypto data and news. Developed for the Fetch.ai Hackathon at Techkriti'25, IIT Kanpur, it demonstrates how multiple microservices can work together to deliver actionable insights. The project now supports querying the price of any cryptocurrency (e.g., BTC, ETH, LTC) and aggregates crypto news using live APIs.

## Agents Overview
  
- **PriceAgent:**  
  Retrieves live cryptocurrency prices using CoinGecko. You can request any coin by passing a query parameter (e.g., `?coin=eth`).  
  _Endpoint:_ [http://localhost:8000/price](http://localhost:8000/price)  
  _Example:_ [http://localhost:8000/price?coin=btc](http://localhost:8000/price?coin=btc)  
  [&#8203;:contentReference[oaicite:0]{index=0}]
  https://agentverse.ai/agents/details/agent1qtws5svef9sd2wx6qxnallkxz9a47h6n2008tkl2c6xx4cshu8jf62wapl8/profile

- **NewsAgent:**  
  Aggregates top crypto news headlines using the NewsAPI.  
  _Endpoint:_ [http://localhost:8001/news](http://localhost:8001/news)  
  **Note:** Set your `NEWS_API_KEY` as an environment variable.  
  [&#8203;:contentReference[oaicite:1]{index=1}]
  https://agentverse.ai/agents/details/agent1qg0ajn45y42vnj3qjgs4rupzd0h7kppxlyzzyx6a0eg6px3xtnja2gnwr05/profile

- **AlertAgent:**  
  Provides a simulated alert message regarding crypto price thresholds.  
  _Endpoint:_ [http://localhost:8002/alert](http://localhost:8002/alert)  
  [&#8203;:contentReference[oaicite:2]{index=2}]
  https://agentverse.ai/agents/details/agent1qfhsk62u4cdc5mh6xglg4kwyu8ddqgpjsckvqjwfgvp0qcqyvqz4xckqxnt/profile

- **AssistantAgent:**  
  Acts as a central coordinator by analyzing user queries. Based on the query, it:
  - Detects a coin symbol (BTC, ETH, etc.) and forwards the request to PriceAgent.
  - Fetches crypto news from NewsAgent.
  - Retrieves alerts from AlertAgent when requested.
  
  _Endpoint:_ [http://localhost:8003/assistant?message=YourQuery](http://localhost:8003/assistant?message=YourQuery)  
  [&#8203;:contentReference[oaicite:3]{index=3}]

## Front End

A simple, polished front end (`index.html`) is provided to interact with the AssistantAgent. It features:
- A clean UI with a text input and a send button.
- Dynamic display of responses (price data, news headlines, and alerts) in a user-friendly format.

Open `index.html` via a local server (e.g., using `python3 -m http.server 5500`) to avoid CORS issues.

## Installation

1. **Clone the Repository:**
   git clone https://github.com/Towaiji/chainwatch-ai.git
   cd chainwatch-ai
Set Up a Virtual Environment (Recommended):

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Dependencies:

pip install -r requirements.txt
Ensure you have FastAPI, uvicorn, and requests installed.

Set Your NewsAPI Key:

export NEWS_API_KEY=your_newsapi_key_here
(On Windows, use the appropriate command for setting environment variables.)

Running the Agents
Open separate terminal windows/tabs and run the following commands:

PriceAgent (Port 8000):

python3 price_agent.py
NewsAgent (Port 8001):

python3 news_agent.py
AlertAgent (Port 8002):

python3 alert_agent.py
AssistantAgent (Port 8003):

python3 assistant_agent.py
Testing the System
You can test the agents individually or as a whole:

Directly via Browser:

PriceAgent: http://localhost:8000/price?coin=eth

NewsAgent: http://localhost:8001/news

AlertAgent: http://localhost:8002/alert

AssistantAgent: http://localhost:8003/assistant?message=What%20is%20the%20price%20of%20BTC%20and%20crypto%20news?

Using the Test Script: Run the provided test_message.py:

python3 test_message.py
This script sends requests to each agent and prints their responses.

Using the Front End: Serve index.html on a local web server:

python3 -m http.server 5500
Then open http://localhost:5500/index.html in your browser, type a query (e.g., "What is the price of ETH and crypto news?"), and click Send Query.

Future Improvements
Multi-Coin Support:
Enhance the PriceAgent to handle more cryptocurrencies using dynamic queries.

Enhanced Assistant:
Improve query parsing to handle a wider variety of questions and combine responses more elegantly.

Real Alerts:
Implement a real-time alerting mechanism based on live data.

UI/UX Upgrades:
Upgrade the front end with a modern framework (e.g., React or Vue) for a richer user experience.

Caching & Rate Limiting:
Add caching to reduce API calls and handle rate limits.

License
This project is licensed under the MIT License.
