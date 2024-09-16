from crewai import Agent,Task,Crew 
from tasks import plan,write,edit 
from agents import planner,writer,editor ;
from dotenv import load_dotenv

import os 

load_dotenv()
os.getenv("GEMINI_API_KEY")

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)

llm = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.1,
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    },
)

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