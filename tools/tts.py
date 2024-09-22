import os
import wave
from dotenv import load_dotenv
from crewai_tools import tool
from deepgram import DeepgramClient, SpeakOptions

load_dotenv()

@tool
def text_to_speech_tool(text: str, filename_template="output_part_{}.wav", final_output="final_output.wav"):
    """
    Tool for converting text to speech using Deepgram API.
    This tool accepts a string of text and converts it into an audio file in .wav format.

    Args:
        text: The text to be converted to speech.
        filename_template: Template for naming the intermediate audio files.
        final_output: Name of the final merged output audio file.

    Returns:
        final_output (str): The name of the final audio file.
    """
    try:
        max_length = 1900
        clean_text = " ".join(text.split())
        words = clean_text.split(' ')
        text_parts = []
        current_part = []

        for word in words:
            if len(' '.join(current_part + [word])) <= max_length:
                current_part.append(word)
            else:
                text_parts.append(' '.join(current_part))
                current_part = [word]
        
        if current_part:
            text_parts.append(' '.join(current_part))

        deepgram = DeepgramClient(api_key=os.getenv("DG_API_KEY"))
        output_files = []

        for i, part in enumerate(text_parts):
            speak_options = {"text": part}
            part_filename = filename_template.format(i + 1)
            output_files.append(part_filename)
            
            options = SpeakOptions(
                model="aura-asteria-en",
                encoding="linear16",
                container="wav"
            )

            deepgram.speak.v("1").save(part_filename, speak_options, options)

        data = []
        for filename in output_files:
            with wave.open(filename, 'rb') as wav_file:
                data.append([wav_file.getparams(), wav_file.readframes(wav_file.getnframes())])
        
        with wave.open(final_output, 'wb') as output_file:
            output_file.setparams(data[0][0])
            for params, frames in data:
                output_file.writeframes(frames)

        return final_output

    except Exception as e:
        return f"Exception: {e}"
