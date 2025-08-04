from crewai import Task

def create_requirement_analysis_task(agent, user_requirement):
    return Task(
        description=(
            f"You received the following requirement:\n\n{user_requirement}\n\n"
            "Break it down into detailed functional modules, edge cases, validations, and interactions."
        ),
        expected_output="A clear breakdown in bullet points or structured format.",
        agent=agent
    )
