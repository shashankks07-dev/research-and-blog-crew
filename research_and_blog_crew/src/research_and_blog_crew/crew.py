from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, task, crew


@CrewBase
class ResearchAndBlogCrew:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        self.my_llm = LLM(
            model="ollama/gemma4",
            base_url="http://localhost:11434"
        )


    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator"], 
            verbose=True,
            llm=self.my_llm
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
            verbose=True,
            llm=self.my_llm
        )

    @task
    def report_task(self) -> Task:
        return Task(config=self.tasks_config["report_task"])

    @task
    def reporting_task(self) -> Task:
        return Task(config=self.tasks_config["reporting_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # one task after another
            verbose=True
        )