from crewai import  Crew, Process
from crewai.project import  crew
from blog_tasks import BlogTasks
from blog_agents import BlogAgents


editor=BlogAgents.editor()
planner=BlogAgents.planner()
writer=BlogAgents.writer()
writeTask = BlogTasks.write(writer)
editTask = BlogTasks.edit(editor)
planTask = BlogTasks.plan(planner)


BlogCrew=Crew(
    agents=[writer,planner,editor],
    tasks=[editTask,writeTask,planTask],
    verbose=True,
    process=Process.sequential
)

input={"topic": "SSH , SSH tunneling, portForwarding and use case of NGRock"}
result=BlogCrew.kickoff(input=input)
print(result); 
