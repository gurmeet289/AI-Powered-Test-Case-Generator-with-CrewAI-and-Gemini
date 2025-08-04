from crewai import Crew
from agents.requirement_analyst import get_requirement_analyst_agent
from agents.test_case_generator import get_test_case_generator_agent
from tasks.requirement_analysis_task import create_requirement_analysis_task
from tasks.test_case_generation_task import create_test_case_generation_task

class CrewManager:
    def __init__(self):
        self.requirement_analyst = get_requirement_analyst_agent()
        self.test_case_generator = get_test_case_generator_agent()

    def run(self, user_requirement):
        requirement_task = create_requirement_analysis_task(self.requirement_analyst, user_requirement)
        test_case_task = create_test_case_generation_task(self.test_case_generator)

        crew = Crew(
            agents=[self.requirement_analyst, self.test_case_generator],
            tasks=[requirement_task, test_case_task],
            verbose=True
        )
        return crew.kickoff()
