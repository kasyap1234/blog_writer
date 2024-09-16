from crewai import Agent 


class BlogAgents():
    def planner(self,llm):
        return Agent(
			role="Content Planner",
			goal=f"Plan engaging and factually accurate content on {topic}",
			backstory=f"You are working on planning a blog article about the topic {topic}...",
			llm=llm,
			allow_delegation=False,
			verbose=True,
		)

    def writer(self,llm) -> Agent:
        return Agent(
			role=f"Content Writer",
			goal="Write insightful and factually accurate opinion piece about the topic: {topic}",
			backstory="You're working on writing a new opinion piece about the topic: {topic} '...",
			allow_delegation=False,
			llm=llm,
			verbose=True,
		)

    def editor(self, llm):
        return Agent(
            role="Editor",
            goal="Edit a given blog post to align with the writing style ,needs to be factually correct and technical explanation needs to be explained with real life examples ",
            backstory="You are an editor who receives a blog post from the Content Writer...",
            llm=llm,
            allow_delegation=False,
            verbose=True,
        )
