from uagents import Agent, Context, Bureau
from fastapi import FastAPI
import asyncio

PRICE_AGENT_ADDR = "agent1q025lcsufwalmspl53usgqvcupkn8qttft3wxy28mxwmtn4dwjlwv0sqv9c"

# Create the Agent
price_agent = Agent(name="PriceAgent", seed="priceagent")

# Define the startup event for the agent
@price_agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("🪙 PriceAgent is live!")

# Create Bureau and add the agent to it
bureau = Bureau()
bureau.add(price_agent)  # Add the agent to the bureau

# Create a FastAPI app to integrate Bureau with Uvicorn
app = FastAPI()

# Use lifespan for startup and shutdown handling
@app.lifespan()
async def lifespan(app: FastAPI):
    # Run Bureau in the background
    await bureau.run_async()  # Bureau starts asynchronously

# This part runs the app and starts the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
