# ChainWatch AI

![tag : innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)

ChainWatch AI is a modular suite of specialized AI agents developed for the Fetch.ai Hackathon at Techkriti'25, IIT Kanpur. This project demonstrates a network of micro-agents that interact to deliver critical insights and notifications for the crypto domain. Each agent is designed for a specific task and can be easily extended or integrated with live data sources.

## Agents

- **PriceAgent**: Provides real-time (mocked) crypto price data. 
https://agentverse.ai/agents/details/agent1qtws5svef9sd2wx6qxnallkxz9a47h6n2008tkl2c6xx4cshu8jf62wapl8/profile
- **NewsAgent**: Aggregates and displays top crypto news headlines. 
https://agentverse.ai/agents/details/agent1qg0ajn45y42vnj3qjgs4rupzd0h7kppxlyzzyx6a0eg6px3xtnja2gnwr05/profile
- **AlertAgent**: Sends alerts when certain price thresholds are reached. 
https://agentverse.ai/agents/details/agent1qfhsk62u4cdc5mh6xglg4kwyu8ddqgpjsckvqjwfgvp0qcqyvqz4xckqxnt/profile
- **AssistantAgent**: Acts as a personalized assistant that processes user messages and is built to dynamically connect with other agents on Agentverse.

## Features

- **Modular Design**: Each agent functions as an independent microservice.
- **Agentverse Integration Ready**: Built to be registered on Agentverse for seamless agent interaction.
- **Proof-of-Concept Focus**: Uses hardcoded (mock) data as a placeholder with plans to integrate live APIs (e.g., crypto price feeds, news sources) in future iterations.
- **Ease of Deployment**: Agents are deployed using FastAPI and uvicorn, making them lightweight and easy to run.

## Architecture

Each agent is implemented as a FastAPI service using the new lifespan event handler pattern:

- **PriceAgent**: Runs on port 8000.
- **NewsAgent**: Runs on port 8001.
- **AlertAgent**: Runs on port 8002.
- **AssistantAgent**: Runs on port 8003.

They communicate with clients via REST endpoints and are designed for easy expansion into a full-fledged network of collaborating agents.

## Installation

1. **Clone the Repository:**
   git clone https://github.com/Towaiji/chainwatch-ai.git
   cd chainwatch-ai

2. **Set Up a Virtual Environment (Optional but Recommended):**
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt
   *Ensure you have FastAPI, uvicorn, and requests installed.*

## Usage

Start each agent in its own terminal window:

- **PriceAgent:**
  python3 price_agent.py

- **NewsAgent:**
  python3 news_agent.py

- **AlertAgent:**
  python3 alert_agent.py

- **AssistantAgent:**
  python3 assistant_agent.py

To quickly test that all agents are running and responding, use the provided test script:
python3 test_message.py
This script sends HTTP GET requests to each agent and prints the JSON responses.

## Future Improvements

- **Live Data Integration**: Replace hardcoded data with live API calls for crypto prices and news.
- **Enhanced Alerting**: Implement dynamic alerts with notifications via multiple channels (email, SMS, etc.).
- **Expanded Assistant**: Enable the AssistantAgent to interact dynamically with other agents on Agentverse for orchestrating complex tasks.
- **Scalability Enhancements**: Refactor the architecture to support more agents and handle higher loads.

## Contribution

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
---

ChainWatch AI is built for the Fetch.ai Hackathon at Techkriti'25, IIT Kanpur. I appreciate your interest and look forward to your feedback!
