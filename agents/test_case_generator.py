from crewai import Agent
from config.llm_config import get_llm

def get_test_case_generator_agent():
    return Agent(
        role="Test Case Generator",
        goal="Generate comprehensive test cases based on user requirement",
        backstory="Skilled in manual and automation-ready test case design.",
        llm=get_llm(),
        verbose=True
    )
