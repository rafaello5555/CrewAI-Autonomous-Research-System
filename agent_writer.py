
from crewai import Agent
from setup_llm import llm


writer_agent = Agent(
  role='Tech Content Strategist',
  goal='Craft well-structured and engaging content based on research findings',
  backstory="""You are a skilled content strategist known for translating 
  complex topics into clear and compelling narratives. Your writing makes 
  information accessible and engaging for a wide audience.""",
  verbose=True,
  llm = llm,
  allow_delegation=True
)

writer_agent
