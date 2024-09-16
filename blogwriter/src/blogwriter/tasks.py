from crewai import Task
from crewai import agents
from agents import Agents 

class BlogTasks:
    def __init__(self, agents):
        self.agents = agents
    @Task
    def plan(self):
        return Task(
            description="1. Prioritize the latest trends, key players, and noteworthy news on {topic}...",
            expected_output="A comprehensive content plan document with an outline, audience analysis, SEO keywords, and resources.",
            agent=self.agents.planner(),
        )
    @Task
    def write(self):
        return Task(
            description="1. Use the content plan to craft a compelling blog post on {topic}...",
            expected_output="A well-written blog post in markdown format, ready for publication, each section should have 2 or 3 paragraphs.",
            agent=self.agents.writer(),
        )
    @Task 
    def edit(self):
        return Task(
            description="Proofread the given blog post for grammatical errors and alignment with the brand's voice.",
            expected_output="A well-written blog post in markdown format, ready for publication, each section should have 2 or 3 paragraphs.",
            agent=self.agents.editor(),
        )
