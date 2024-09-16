from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tasks import BlogTasks

writeTask = BlogTasks.write()
editTask = BlogTasks.edit()
planTask = BlogTasks.plan()


@CrewBase
class BlogwriterCrew:

    @crew
    def crew(self) -> Crew:
        """Creates the Blogwriter crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
