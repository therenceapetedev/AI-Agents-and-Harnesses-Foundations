import os

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("Hello from ai-agents-and-harnesses-foundations!")
    print(os.environ.get("ANTHROPIC_API_KEY"))
