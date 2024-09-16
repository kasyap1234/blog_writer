from crewai import agent, agents
from crewai import Agent

class BlogAgents:
	def __init__(self, llm) -> None:
		self.llm = llm

	@agent
	def planner(self):
		return Agent(
			role="Content Planner",
			goal="Plan engaging and factually accurate content on {topic}",
			backstory="You are working on planning a blog article about the topic {topic}...",
			llm=self.llm,
			allow_delegation=False,
			verbose=True,
		)

	@agent
	def editor(self):
		return Agent(
			role="Editor",
			goal="Edit a given blog post to align with the writing style ,needs to be factually correct and technical explanation needs to be explained with real life examples ",
			backstory="You are an editor who receives a blog post from the Content Writer...",
			llm=self.llm,
			allow_delegation=False,
			verbose=True,
		)

	@agent
	def writer(self) -> Agent:
		return Agent(
			role="Content Writer",
			goal="Write insightful and factually accurate opinion piece about the topic: {topic}",
			backstory="You're working on writing a new opinion piece about the topic: {topic} '...",
			allow_delegation=False,
			llm=self.llm,
			verbose=True,
		)