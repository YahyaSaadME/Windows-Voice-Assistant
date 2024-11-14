import speech_recognition as sr
from click import find_and_click

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Increased duration for ambient noise adjustment
        print("Say something...")

        try:
            audio_data = recognizer.listen(source, timeout=10)  # Added timeout for listening
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            return 1

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)
        print(f"You said: {text}")
        print('Converting....')
        return text

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return 1
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return 1
        
    return 0  # Return 0 to indicate success

# recognize_speech()