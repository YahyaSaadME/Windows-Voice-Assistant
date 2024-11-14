'''
import tkinter as tk
from PIL import Image, ImageTk
import threading

from speech import recognize_speech

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        
        # Make the window always on top
        self.root.attributes("-topmost", True)
        
        # Set the size of the window and background color
        self.root.geometry("250x70+1600+900")  # Width x Height + X_offset + Y_offset
        self.root.configure(bg='white')  # Set background color to white
        
        # Create a microphone button
        self.mic_button = tk.Button(self.root, command=self.start_voice_assistant, borderwidth=0, bg='white', activebackground='lightgray')
        
        # Load microphone icon
        self.mic_icon = Image.open("mic_icon.png")  # Replace with your microphone icon path
        self.mic_icon = self.mic_icon.resize((20, 20))
        self.mic_photo = ImageTk.PhotoImage(self.mic_icon)
        
        # Set the icon on the button
        self.mic_button.config(image=self.mic_photo)
        self.mic_button.pack(pady=20)  # Center the button vertically in the window

    def start_voice_assistant(self):
        # Change the button text to "Listening..."
        self.mic_button.config(text="Listening...", image='', bg='lightgray')
        self.root.update()  # Force update the GUI
        
        # Start speech recognition in a separate thread
        threading.Thread(target=self.listen_for_speech, daemon=True).start()

    def listen_for_speech(self):
        if recognize_speech():
            self.root.after(0, self.stop_listening)  # Schedule GUI update on the main thread

    def stop_listening(self):
        self.mic_button.config(text='', image=self.mic_photo, bg='white')
        
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()
'''
import tkinter as tk
from PIL import Image, ImageTk
import threading
import pygame
from speech import recognize_speech

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Make the window always on top
        self.root.attributes("-topmost", True)
        
        # Set the size of the window and background color
        self.root.geometry("250x70+1600+900")  # Width x Height + X_offset + Y_offset
        self.root.configure(bg='white')  # Set background color to white
        
        # Create a microphone button
        self.mic_button = tk.Button(self.root, command=self.start_voice_assistant, borderwidth=0, bg='white', activebackground='lightgray')
        
        # Load microphone icon
        self.mic_icon = Image.open("mic_icon.png")  # Replace with your microphone icon path
        self.mic_icon = self.mic_icon.resize((20, 20))
        self.mic_photo = ImageTk.PhotoImage(self.mic_icon)
        
        # Set the icon on the button
        self.mic_button.config(image=self.mic_photo)
        self.mic_button.pack(pady=20)  # Center the button vertically in the window

    def play_sound_in_background(self):
        # Load the Bing sound
        pygame.mixer.music.load('ding.mp3')
        
        # Play the sound
        pygame.mixer.music.play()
        
        # Wait until the sound finishes playing
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(1)

    def play(self):
        # Create a daemon thread to run the play_sound_in_background function
        sound_thread = threading.Thread(target=self.play_sound_in_background)
        sound_thread.daemon = True
        sound_thread.start()

    def start_voice_assistant(self):
        # Change the button text to "Listening..."
        self.mic_button.config(text="Listening...", image='', bg='lightgray')
        self.root.update()  # Force update the GUI
        
        # Play the sound
        self.play()
        
        # Start speech recognition in a separate thread
        threading.Thread(target=self.listen_for_speech, daemon=True).start()

    def listen_for_speech(self):
        self.data = recognize_speech()
        print(self.data)
        if self.data:
            self.root.after(0, self.stop_listening)  # Schedule GUI update on the main thread

    def stop_listening(self):
        print(self.data)
        if type(self.data) == str:
            self.mic_button.config(text=(self.data[:20]+('...'if len(self.data) > 20 else '' )), image=self.mic_photo, bg='white')
        else:
            self.mic_button.config(text='', image=self.mic_photo, bg='white')
        
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()