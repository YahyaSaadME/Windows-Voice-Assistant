import speech_recognition as sr
import pygame
import threading
import time
from speech import recognize_speech
from audio import convert_text_to_speech
from click import find_and_click
from execute import execute_key_combinations
from convert import groq

pygame.mixer.init()
recognizer = sr.Recognizer()

def play_sound_in_background():
    pygame.mixer.music.load('ding.mp3')  # Or 'bing_sound.wav'
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(1)

def play():
    sound_thread = threading.Thread(target=play_sound_in_background)
    sound_thread.daemon = True  # Set the thread as a daemon thread
    sound_thread.start()

def req(res):
    try:
        if('click' in res[:5]):
            convert_text_to_speech('ok')
            res = res.replace('click on','').replace('click','')
            find_and_click(res)
            
        res = groq.chat(res)
        for r in res:
            try:
                if 'audio' in r.keys():
                    try:
                        convert_text_to_speech(r['audio'])
                    except Exception as e:
                        print(f'Error getting the audio: {e}')
                        
                elif 'gui' in r.keys():
                    try:
                        convert_text_to_speech('ok')
                        execute_key_combinations(r['gui'])
                    except Exception as e:
                        convert_text_to_speech("Sorry i can't do that")
                        print(f'Error executing the command: {e}')
                        
                elif 'ocr' in r.keys():
                    try:
                        convert_text_to_speech('ok')
                        find_and_click(r['ocr'])
                    except Exception as e:
                        print(f'Error executing the command: {e}')
                        
                else:
                    convert_text_to_speech("Sorry i can't do that")
                    print('Error in the response')
                
                time.sleep(1)
            except Exception as es:
                print('es:',es)
                convert_text_to_speech("Sorry i can't do that")
    except Exception as e:
        print('e:',e)
        convert_text_to_speech("Sorry i can't do that")
        
def listen_for_alexa():
    with sr.Microphone(sample_rate=16000) as source:
        print("Listening for 'Alexa'...")  # Feedback to the user
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for audio input

    try:
        speech_text = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {speech_text}")

        if "alexa" in speech_text.lower():
            play() 
            print("Alexa heard! Triggering action.")
           
            if len(speech_text.lower()) > 5 :   
                res = speech_text.lower().replace('alexa','')
                req(res)
            else:
                req(recognize_speech())  # Call the recognize_speech function
    
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")

while True:
    listen_for_alexa()