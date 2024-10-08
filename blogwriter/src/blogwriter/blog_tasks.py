from crewai import Task



class BlogTasks():
    
  
    def plan(self,agent):
        return Task(
            description="1. Prioritize the latest trends, key players, and noteworthy news on {topic}...",
            expected_output="A comprehensive content plan document with an outline, audience analysis, SEO keywords, and resources.",
            agent=agent 
        )
   
    def write(self,agent):
        return Task(
            description="1. Use the content plan to craft a well detailed,technical and compelling blog post on {topic},it should be explained in a detailed manner with real life examples . ",
            expected_output="A well-written detailed blog post in markdown format, ready for publication, each section should have 2 or 3 paragraphs.",
            agent=agent
        )
    
    def edit(self,agent):
        return Task(
            description="Proofread the given blog post for grammatical errors and alignment for developers . ",
            expected_output="A well-written detailed blog post in markdown format, ready for publication, each section should have 2 or 3 paragraphs.",
            agent=agent 
        )
