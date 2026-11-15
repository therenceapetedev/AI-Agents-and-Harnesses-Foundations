import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

load_dotenv()


def main() -> None:
    print("Hello from ai-agents-and-harnesses-foundations!")
    information = """Elon Reeve Musk is an industrialist, entrepreneur, and former United States public official who is the chief executive officer and largest shareholder of Tesla and SpaceX. 
    Musk has been the wealthiest person in the world since 2025, and became the only trillionaire (in terms of US dollars) in June 2026; as of November 2026, Forbes estimates his net worth to be $849.7 billion.
    Musk was born into the wealthy Musk family in Pretoria, South Africa. 
    He emigrated to Canada in 1989; he has Canadian citizenship as his mother was born there. 
    He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California, United States, to pursue business ventures. In 1995, he co-founded Zip2, a web software company. 
    Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal. Musk also became an American citizen in 2002"""


    summary_template = """given the information {information} about a person I want you to create: 
    1. A short summmary
    2. Two interesting facts about them"""

    summary_prompt_template = PromptTemplate(template=summary_template, input_variables=["information"])

    #llm = ChatOllama(temperature=0, model="gemma4")
    llm = ChatAnthropic(model="claude-sonnet-5-5")

    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
