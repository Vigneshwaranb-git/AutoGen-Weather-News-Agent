import asyncio
from ddgs import DDGS
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Web search tool
def search_weather_news(city:str)->str:
    """Search the web for weather news"""
    return str(DDGS().news(query=f"{city} weather today", max_results=5))

city= input("Which City? ")

# Model Client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

# Agent
agent = AssistantAgent(
    name="weather_news",
    model_client=model_client,
    tools=[search_weather_news],
    system_message="You are an expert weather news resercher. Search the web for the weather news for given city. Reply news in 3-points in professional",
    reflect_on_tool_use=True
)

async def main():
    await Console(agent.run_stream(
        task=f"Search weather news for {city} and Reply news in 3-points in professional"
    ))
    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())

