import pyttsx3

engine = pyttsx3.init() # Here this is intitialize object.
# We can initialize object like this objectname = pyttsx.init()
# If we want to change voice then we do like this :
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[3].id)
engine.say("Hi, I am Dhruvil Dobariya.")
engine.say("My father name is Arvindbhai Dobariya")
engine.say("Thank you!")
engine.runAndWait()