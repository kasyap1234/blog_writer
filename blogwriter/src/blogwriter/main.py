from crewai import  Crew, Process
from crewai.project import  crew
from blog_tasks import BlogTasks
from blog_agents import BlogAgents
from langchain_ollama import ChatOllama
import os

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(model="gemma2:2b", base_url="http://localhost:11434")
blog_agents=BlogAgents()
blog_tasks=BlogTasks()
editor=blog_agents.editor(llm)
planner=blog_agents.planner(llm)
writer=blog_agents.writer(llm)
writeTask = blog_tasks.write(writer)
editTask = blog_tasks.edit(editor)
planTask = blog_tasks.plan(planner)


BlogCrew=Crew(
    agents=[planner,writer,editor],
    tasks=[planTask,editTask,writeTask],
    verbose=True,
    process=Process.sequential
)

input={"topic": "SSH , SSH tunneling, portForwarding and use case of NGRock"}
result=BlogCrew.kickoff(inputs=input)

print(result); 
