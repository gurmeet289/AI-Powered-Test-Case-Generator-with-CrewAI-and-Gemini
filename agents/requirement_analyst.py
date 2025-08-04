from crewai import Agent
from config.llm_config import get_llm

def get_requirement_analyst_agent():
    return Agent(
        role="Requirement Analyst",
        goal="Break down user requirements into clear functional components",
        backstory="An expert in software analysis with attention to detail.",
        llm=get_llm(),
        verbose=True
    )
