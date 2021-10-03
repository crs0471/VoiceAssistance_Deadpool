import pandas as pd
import random

data = pd.read_csv("commands.csv",names=['keyword','reply'])
keywords = list(data['keyword'])
replys = list(data['reply'])

def fetch(cmd):
    reply = "sorry sir , I can't understand what you are saying."
    for i in keywords:
        print(i)
        if i in cmd:
            ind = keywords.index(i)
            break
    fetched_reply = str(data['reply'][ind])
    list_reply = fetched_reply.split("|")
    print(list_reply)
    reply = random.choice(list_reply).lower().strip()
    return reply

#print(fetch(' what is your favrate show'))
