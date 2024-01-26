# Chatbot Assistant with Voice Recognition

## Introduction
This is a Python-based chatbot assistant that uses voice recognition to take commands and provide responses. The assistant can perform various tasks such as answering questions, telling the time, date, weather information, opening websites, and more.

## Features
- Voice recognition using the `speech_recognition` library.
- Text-to-speech using the `pyttsx3` library.
- Integration with Wikipedia for information retrieval.
- Opening various websites like Google, YouTube, etc.
- Weather information retrieval using the Weather API.
- News headlines retrieval using the News API.

## Dependencies
- `pyttsx3`: Text-to-speech library for Python.
- `speech_recognition`: Library for performing speech recognition.
- `wikipedia`: Library for accessing and parsing Wikipedia articles.
- `webbrowser`: Module for opening and displaying web-based documents.
- `requests`: Library for making HTTP requests.
- `json`: Module for working with JSON data.
- `googlesearch-python`: Library for programmatically performing Google searches.

## Usage
1. Install the required dependencies using the following command:
    ```
    pip install pyttsx3 SpeechRecognition wikipedia googlesearch-python
    ```
2. Run the `main.py` file to start the chatbot.

## Commands
- **Time**: Ask for the current time.
- **Date**: Ask for the current date.
- **Weather**: Get the current weather information for a specific city.
- **News**: Retrieve top news headlines in various categories.
- **Open [Website]**: Open specific websites like Google, YouTube, etc.
- **Search [Query]**: Perform a Google search for the given query.
- **Play [Song]**: Open and play search results for a specific song.
- **Sing [Language] Song**: Have the chatbot sing a song in Hindi, English, Bengali, or Tamil.
- **Exit/Quit/Stop**: Exit the chatbot.

## Voice Commands
The chatbot responds to voice commands. Speak clearly and wait for the chatbot to recognize your command before proceeding.
EXAMPLE : 
- For know about news say "current news today" .
- For know about weather report say "what is the weather condition in 'palce name like kolkata, mumbai ,london'" .
- For open any website just say "open 'website name like youtube,google,geeksforgeeks'".
- For playing any music say "play 'song name'".

## Ingredients

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>

Feel free to contribute or open issues if you encounter any problems!
