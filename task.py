from crewai import Task
from agent_researcher import researcher_agent
from agent_writer import writer_agent



from dotenv import load_dotenv
import os

load_dotenv()  # load keys from .env

serper_key = os.getenv("SERPER_API_KEY")
watson_key = os.getenv("WATSONX_API_KEY")

print("Serper key loaded:", serper_key is not None)
print("Watson key loaded:", watson_key is not None)






researcher_task = Task(
  description="Analyze the major {topic}, identifying key trends and technologies. Provide a detailed report on their potential impact.",
  agent=researcher_agent,
  expected_output="A detailed report on {topic}, including trends, emerging technologies, and their impact."
)


writer_task = Task(
  description="Create an engaging blog post based on the research findings about {topic}. Tailor the content for a tech-savvy audience, ensuring clarity and interest.",
  agent=writer_agent,
  expected_output="A 4-paragraph blog post on {topic}, written clearly and engagingly for tech enthusiasts."
)


from crewai import Crew, Process

crew = Crew(
    agents=[researcher_agent, writer_agent],
    tasks=[researcher_task, writer_task],
    process=Process.sequential,
    verbose=True 
)

result = crew.kickoff(inputs={"topic": "Will AI replace human in future in industry?"})

type(result)
result