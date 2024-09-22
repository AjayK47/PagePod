# PagePod: Multi-Agent Web content Audio Synthesizer

This project uses a multi-agent framework to automatically generate podcasts from website content. It leverages the power of AI to scrape web content, refine it, create a script, and convert it to speech.

## Features

- Web scraping of content
- Content refinement and validation
- Automatic podcast script generation
- Script validation and improvement
- Text-to-speech conversion
- Multi-agent system using CrewAI

## Prerequisites

- Python 3.7+
- [OpenAI API key](https://platform.openai.com/) or [Groq API key](https://console.groq.com/keys)
- [Deepgram API key](https://deepgram.com/product/text-to-speech)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/multi-agent-podcast-generator.git
   cd multi-agent-podcast-generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   DG_API_KEY=your_deepgram_api_key
   ```

## Usage

Run the main script:

```
python main.py
```

You will be prompted to enter a URL. The system will then:
1. Scrape the content from the provided URL
2. Refine and validate the content
3. Generate a podcast script
4. Convert the script to speech
5. Save the resulting audio file

## Project Structure

- `main.py`: Entry point of the application
- `agents.py`: Defines the AI agents used in the process
- `tasks.py`: Defines the tasks for each agent
- `tools/tts.py`: Contains the text-to-speech tool
- `requirements.txt`: Lists all Python dependencies

## Customization

You can customize the behavior of the agents by modifying their roles, goals, and backstories in the `agents.py` file. You can also adjust the task descriptions in `tasks.py` to fine-tune the process.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- OpenAI for the language model
- Deepgram for the text-to-speech API
