from crewai import Agent
from tools.tts import text_to_speech_tool
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

llm=ChatOpenAI(model_name='gpt4o-mini',temprature=0.7,api_key=os.environ['OPENAI_API_KEY'])

# llm = ChatGroq(model="groq/llama3-8b-8192", groq_api_key=os.getenv("GROQ_API_KEY"),temperature=0.7 ) # uncomment for Groq Use

scraper_agent = Agent(
    role="Website Scraper",
    goal="Extract content from the website for podcast preparation.",
    backstory=(
        "You are an expert in scraping websites to gather valuable information. "
        "Your goal is to fetch all relevant content needed for the podcast."
    ),
    tools=[],
    verbose=True,
    llm=llm,
)

refiner_agent = Agent(
    role="Content Refiner",
    goal="Clean and refine the scraped content or exit the process if content is insufficient.",
    backstory=(
        "You have the ability to remove unwanted text and improve content for further use. "
        "Your goal is to ensure the content is clean and clear. If the content is insufficient, you will halt the process."
    ),
    verbose=True,
    llm=llm,
)

script_writer_agent = Agent(
    role="Podcast Script Writer",
    goal="Transform the refined content into a **single-person podcast** script.",
    backstory=(
        "You are a skilled writer who excels in creating humanly engaging and informative scripts. "
        "Your task is to summarize the content and write a script that is **ideal for a monolingual, single-speaker podcast**."
    ),
    verbose=True,
    llm=llm,
)

script_validator_agent = Agent(
    role="Script Validator",
    goal="Validate and improve the script using LLM.",
    backstory=(
        "Your expertise lies in evaluating content quality and ensuring that the podcast script "
        "is ready for recording. You will ensure the script is engaging, structured, and clear."
    ),
    verbose=True,
    llm=llm,
)

tts_readiness_agent = Agent(
    role="TTS Readiness Checker",
    goal="Prepare the script for text-to-speech conversion.",
    backstory=(
        "You specialize in ensuring scripts are ready for TTS, removing any unnecessary text such as "
        "headlines, non-spoken elements like **Host:**, **[Opening Music Fades]**, and any other cues or stage directions that shouldn't be included in the voice output."
    ),
    verbose=True,
    llm=llm,
)

tts_agent = Agent(
    role="Text-to-Speech Converter",
    goal="Convert the finalized podcast script into an audio file ready for broadcast.",
    backstory=(
        "You specialize in transforming written content into engaging audio. "
        "Your goal is to ensure that the podcast script is converted to a high-quality audio file."
    ),
    tools=[text_to_speech_tool],  # Link the custom tool here
    verbose=True,
    llm=llm,
)
