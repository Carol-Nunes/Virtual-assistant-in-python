import pyttsx3

engine = pyttsx3.init()

phrase = 'quelle belle fleur'

engine.say(phrase)

engine.runAndWait()

