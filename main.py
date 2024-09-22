import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import scraper_agent, refiner_agent, script_writer_agent, script_validator_agent, tts_readiness_agent, tts_agent
from tasks import scrape_content_task, refine_content_task, write_podcast_script_task, validate_script_task, prepare_for_tts_task, tts_task
from crewai_tools import ScrapeWebsiteTool


# Load environment variables
load_dotenv()

# Get the URL input from the user
url = input("Enter the URL to scrape: ")

# Initialize the scraping tool
scrape_tool = ScrapeWebsiteTool(website_url=url)

# Assign the tool to the scraper agent
scraper_agent.tools = [scrape_tool]

# Crew creation and process setup
crew = Crew(
    agents=[scraper_agent, refiner_agent, script_writer_agent, script_validator_agent, tts_readiness_agent, tts_agent],
    tasks=[scrape_content_task, refine_content_task, write_podcast_script_task, validate_script_task, prepare_for_tts_task, tts_task],
    process=Process.sequential,  # Ensures tasks run in order
)

# Kickoff the process
crew.kickoff()
