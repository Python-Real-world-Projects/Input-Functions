import speech_recognition as sr
from gtts import gTTS
import pygame

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize pygame mixer
pygame.mixer.init()

def listen():
    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

    try:
        # Recognize the audio and convert it to text
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return f"Sorry, there was an error with the speech recognition service: {str(e)}"

def respond(user_input):
    # Define some simple responses based on keywords
    if "how are you" in user_input:
        response = "I'm just a computer program, but I'm doing well. How can I assist you?"
    elif "hello" in user_input:
        response = "Hello! How can I help you today?"
    else:
        response = "I'm not sure how to respond to that."

    # Convert text to speech and play the response audio using pygame
    tts = gTTS(response)
    tts.save("response.mp3")
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    while True:
        user_input = listen()
        print(f"You said: {user_input}")
        respond(user_input)
