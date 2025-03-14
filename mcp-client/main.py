import asyncio
import os
import click

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")


def parse_ai_messages(data):
    messages = dict(data).get('messages', [])
    formatted_ai_responses = []

    for message in messages:
        if isinstance(message, AIMessage):
            if message.content:
                formatted_message = f"### AI Response:\n{'*'*90}\n{message.content}\n{'*'*90}\n"
                formatted_ai_responses.append(formatted_message)

    return formatted_ai_responses


async def main(prompt: str):
    file_path = os.path.dirname(os.path.abspath(__file__))
    async with MultiServerMCPClient(
        {
            "bmi": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": [ f"{file_path}/bmi_server.py"],
                "transport": "stdio",
            },
            "mysql_server": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            }
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        agent_response = await agent.ainvoke({"messages": f"{prompt}"})
        parsed_data = parse_ai_messages(agent_response)
        for ai_msg in parsed_data:
            print(ai_msg)

if __name__ == "__main__":
    while True:
        prompt = click.prompt("Please enter your prompt. E.g. get all content from database containing Kasper", type=click.STRING)
        asyncio.run(main(prompt))
        if not click.confirm("Do you want to perform another task?"):
            break
   