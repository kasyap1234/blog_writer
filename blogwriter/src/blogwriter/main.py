#!/usr/bin/env python
import sys
from crew import BlogwriterCrew
from crew import BlogwriterCrew
from langchain_ollama import ChatOllama

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    BlogwriterCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        BlogwriterCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BlogwriterCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        BlogwriterCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


# Initialize the LLM
llm = ChatOllama(model="gemma2", base_url="http://localhost:11434")

# Create an instance of BlogwriterCrew
blogwriter_crew = BlogwriterCrew(llm=llm)

# Get the crew
crew = blogwriter_crew.crew()

# Define your inputs
inputs = {"topic": "SSH, port forwarding and use of NGrock"}

# Kickoff the crew
result = crew.kickoff(inputs=inputs)
print(result)
