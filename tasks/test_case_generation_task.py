from crewai import Task

def create_test_case_generation_task(agent):
    return Task(
        description=(
            "Use the requirement breakdown to create:\n"
            "- Functional Test Cases\n"
            "- Edge Case Scenarios\n"
            "- Validations\n"
            "- Positive & Negative Test Cases"
        ),
        expected_output="A structured list of test cases with titles, steps, and expected results.",
        agent=agent
    )
