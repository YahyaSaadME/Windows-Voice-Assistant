import pyttsx3

def convert_text_to_speech(text, speak_faster=True):
    """
    Converts the given text to speech and plays the audio.
    
    Parameters:
    text (str): The text to be converted to speech.
    speak_faster (bool, optional): If True, the speech will be played slightly faster. Defaults to True.
    """
    engine = pyttsx3.init()
    
    # Set the speech rate
    if speak_faster:
        engine.setProperty('rate', engine.getProperty('rate') + 10)
    
    engine.say(text)
    engine.runAndWait()