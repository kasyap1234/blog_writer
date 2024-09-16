from crewai import Agent,Task,Crew 
from tasks import plan,write,edit 
from agents import planner,writer,editor ;
from dotenv import load_dotenv

import os 

load_dotenv()
os.getenv("GEMINI_API_KEY")

from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma2", base_url="http://localhost:11434")

crew=Crew(
    agents=[planner,writer,editor],
    tasks=[plan,write,edit],
    llm=llm,
    verbose=True
)

inputs={
    "topic": "SSH , port forwarding and use of NGrock"
}
crew.kickoff(inputs=inputs)
