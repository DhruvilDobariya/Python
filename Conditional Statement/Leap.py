import pyttsx3

engine = pyttsx3.init()

year = int(input("Enter a year : "))
if year%4 == 0:
    print("{} is a leap year.".format(year))
    engine.say("{} is a leap year.".format(year))
else:
    print("{} is not a leap year".format(year))
    engine.say("{} ia not a leap year.".format(year))
engine.runAndWait()