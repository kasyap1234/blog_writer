from crewai import Agent 


class BlogAgents():
    def planner(self,llm):
        return Agent(
			role="Content Planner",
			goal="Plan engaging and factually accurate content on {topic}",
			backstory="You are working on planning a blog article about the topic {topic}...",
			llm=llm,
			allow_delegation=False,
			verbose=True,
		)

    def writer(self,llm) -> Agent:
        return Agent(
			role="Content Writer",
			goal="Write insightful and factually accurate and detailed opinion piece about the topic: {topic}",
			backstory="You're working on writing a new opinion piece about the topic: {topic} '...",
			allow_delegation=False,
			llm=llm,
			verbose=True,
		)

    def editor(self, llm):
        return Agent(
            role="Editor",
            goal="Edit a given blog post to align with the writing style and the target audience is software developers  ,needs to be factually correct and technical explanation needs to be explained with real life examples ",
            backstory="You are an editor who receives a blog post from the Content Writer...",
            llm=llm,
            allow_delegation=False,
            verbose=True,
        )
