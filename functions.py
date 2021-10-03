import speech_recognition as sr

#Speech to text
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Deadpool : Listening.....")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"boss : {query}")
            return query
        except:
            print("Try Again..")

#command()  ##uncoment to test above functions

#text to speech
import pyttsx3 as pt
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
engine.setProperty("rate", 170)
def speak(audio):
    engine = pt.init()
    print(f"Deadpool :  {audio}")
    engine.say(audio)
    engine.runAndWait()


#speak("hello my name is Deadpool") #uncomment this to  test above functions

