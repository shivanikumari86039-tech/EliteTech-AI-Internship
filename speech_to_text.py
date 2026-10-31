
# Project: Speech Recognition System
# Internship: EliteTech AI Internship
# Task 2

import speech_recognition as sr
from pathlib import Path


def recognize_speech(audio_file):
    """Convert audio speech into text."""

    file_path = Path(audio_file)

    # Check whether the audio file exists.
    if not file_path.exists():
        return "Error: Audio file not found."

    recognizer = sr.Recognizer()

    try:
        # Load the audio file.
        with sr.AudioFile(str(file_path)) as source:
            print("Reading audio file...")
            audio = recognizer.record(source)

        # Convert speech into text.
        print("Recognizing speech. Please wait...")

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:
        return "Sorry, speech could not be understood."

    except sr.RequestError as error:
        return f"Service error: {error}"

    except (OSError, ValueError) as error:
        return f"Audio file error: {error}"


def main():

    print("=" * 45)
    print("       SPEECH RECOGNITION SYSTEM")
    print("       EliteTech AI Internship")
    print("=" * 45)

    audio_file = input(
        "\nEnter audio filename (sample_audio.wav): "
    ).strip().strip('"')

    result = recognize_speech(audio_file)

    print("\n----------- RESULT -----------")
    print("Recognized Text:", result)
    print("------------------------------")


if __name__ == "__main__":
    main()
