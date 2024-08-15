# import speech_recognition as sr

from gtts import gTTS
import os
from io import BytesIO
from playsound import playsound
import pyttsx3


language = 'en'

# def speech_to_text():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         print("Please say something....")
#         audio = recognizer.listen(source, timeout=2)
#         try:
#             print("You said: \n" + recognizer.recognize_google(audio))
#             return (recognizer.recognize_google(audio))
#         except Exception as e:
#             print("Error: " + str(e))

def text_to_speech(text):
    output = gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
    playsound("output.mp3")

def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"{filepath} has been deleted.")
    else:
        print(f"The file {filepath} does not exist.")

def speak_fast(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', rate+50)  # setting up new voice rate
    engine.say(text)
    engine.runAndWait()


def main():  
    # text_to_
    speak_fast("Testing, Testing, Testing")
    # speech("Testing, Testing, Testing")
    # text_to_speech("fak")

if __name__ == "__main__":
    main()
