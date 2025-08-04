from crewai import LLM

def get_llm():
    return LLM(
        model="gemini/gemini-2.0-flash",
        temperature=0.3
    )
