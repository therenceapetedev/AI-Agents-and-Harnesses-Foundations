from dotenv import load_dotenv
from langchain.agents import create_agent 
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_anthropic import ChatAnthropic
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient()

def main() -> None:
    print("Hello from project-search-agent!")
    llm = ChatAnthropic(model="claude-sonnet-5-5")
    tools = [search]
    agent = create_agent(model=llm, tools=tools)
    result= agent.invoke({"messages": [HumanMessage(content="Search for 3 job postings for an AI engineer in LangChain in the Bay Area on LinkedIn and list all of their details." )]})
    print(result)

@tool
def search(query: str) -> str:
    """
Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
"""
    print(f"Searching for: {query}")
    return tavily.search(query=query)

if __name__ == "__main__":
    main()