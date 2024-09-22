from crewai import Task
from agents import scraper_agent, refiner_agent, script_writer_agent, script_validator_agent, tts_readiness_agent, tts_agent

scrape_content_task = Task(
    description=(
        "Scrape the content of the website from the provided link using ScrapeWebsiteTool. "
        "Ensure you capture the main text of the article for podcast preparation."
    ),
    expected_output="A clean version of the content in plain text format.",
    agent=scraper_agent
)

refine_content_task = Task(
    description=(
        "Refine the scraped content and assess if it is sufficient for script writing. "
        "If the content is insufficient, stop further processing."
    ),
    expected_output="A clean and polished version of the content ready for script creation.",
    agent=refiner_agent,
    inputs={"content": "{{scrape_content_task.output}}"},
    tools=[]
)

write_podcast_script_task = Task(
    description=(
        "Create a humanly engaging podcast script based on the refined content. "
        "This script should be conversational, easy to follow, and written specifically for a **single speaker podcast** format. "
        "Ensure there are no interactions between multiple hosts or speakers, and the language remains monolingual."
    ),
    expected_output="A well-structured, conversational script ready for a monolingual podcast narration.",
    agent=script_writer_agent,
    inputs={"refined_content": "{{refine_content_task.output}}"}
)

validate_script_task = Task(
    description=(
        "Validate the podcast script for engagement, structure, and clarity using LLM. "
        "Ensure the script is monolingual and written for a single speaker. "
        "Refine the script further if necessary to improve quality."
    ),
    expected_output="A validated and improved podcast script ready for recording.",
    agent=script_validator_agent,
    inputs={"script": "{{write_podcast_script_task.output}}"}
)

prepare_for_tts_task = Task(
    description=(
        "Ensure the podcast script is ready for TTS conversion by removing any text cues like **Host:**, "
        "**[Opening Music Fades In and Out]**, and any other stage directions, headlines, or markers that shouldn't be included in the voice recording. "
        "The final output should only include text that will be spoken by a human."
    ),
    expected_output="A script fully ready for text-to-speech conversion, containing only spoken text.",
    agent=tts_readiness_agent,
    inputs={"validated_script": "{{validate_script_task.output}}"}
)

tts_task = Task(
    description=(
        "Convert the validated podcast script into an audio file. "
        "Ensure the audio is clear and properly formatted for a single-person podcast."
    ),
    expected_output="An audio file in .wav format ready for broadcast.",
    agent=tts_agent,
    inputs={"validated_script": "{{validate_script_task.output}}"}
)
