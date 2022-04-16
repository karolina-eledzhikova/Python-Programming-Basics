import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # getting details of current voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() # Without this command, speech will not be audible to us
if __name__=="__main__" :
    speak("Here's to another year of friendship, laughter, and getting up to no good together! Happy Birthday, dear Ketiiii!")