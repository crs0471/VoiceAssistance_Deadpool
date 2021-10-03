import wikipedia
import pyjokes
import random
import requests
import datetime
import os

from functions import command, speak
from fatch_ans_and_prosecc import fetch

speak("hello sir, How can i help you?")
while True:
    query = command().lower()

    # normal
    if 'name' in query:
        speak("hello, my name is  deadpool.")
    elif 'are you single' in query:
        answere = ['once i proposed basanti but she said "sorry, i have boyfriend " so unfortunately yes, i am single  ','you will make me cry']
        speak(random.choice(answere))
    elif 'hate' in query:
        speak("I hate when someone says 'I hate garba'")
    elif 'love' in query:
        speak("i Love everything which make you smile")
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"it's {time} boss.")

    # who is  or what is or which is

    elif 'who is' in query and 'wikipedia' in query:
        query = query.replace('who is',"")
        speak(wikipedia.summary(query,2))
    elif 'what is' in query and 'wikipedia' in query:
        query = query.replace('what is', "")
        speak(wikipedia.summary(query,2))
    elif 'which is' in query and 'wikipedia' in query:
        query = query.replace('which is', "")
        speak(wikipedia.summary(query,2))

    #joke

    elif 'joke' in query:
        speak(pyjokes.get_joke())
        print("joke")

    #news

    elif 'news' in query:
        def trandnews():
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
            page = requests.get(url).json()
            article = page["articles"]
            results = []
            for ar in article:
                results.append(ar['title'])
            for i in range(len(results)):
                print(i + 1 , results[i])
            speak("here are the top news...!")
            speak("do you want me to read?")
            reply = command().lower()
            reply =str(reply)
            if reply == "yes" or reply == "ya":
                speak(results)
            else:
                speak("ok!!!")
                pass
        trandnews()

    # music

    elif 'music' in query:
        music_dir = "/home/crs/Music"
        songs = os.listdir(music_dir)
        song = random.randint(0,len(songs)-1)
        print(songs[song])
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir,songs[0]))

    elif "bye" in query:
        answere = ['bye bye','have a good day','see ya soon','bye nice to talk with you']
        speak(random.choice(answere))

    #from csv file
    else:
        speak(fetch(query))

