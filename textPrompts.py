import datetime
import time as t

def dailyRoutine():
    while 1:
        time = str(datetime.datetime.now())[10:15]
        checkTime(time)
        t.sleep(20)
        
        #question types ratings, reminder, yn
def responder(qtype, response):
    if qtype == 'rating':
        print(" \n")
        used = input() 
        print(used)
    if qtype == 'dialog':
        print(response)
    if qtype == 'yn':
        print(response)
    
def checkTime(time):
    if time == "09:0":
        print(time)
        sender(questions["rating"])
        x = responder("rating", questions["rating"])
    elif time == "01:0":
        print(time)
    elif  time == "18:0":
        print(time)
    elif time == "22:0":
        print(time)
    elif time == "15:5":
        print(time)
    else:
        print(time)
        sender(questions["rating"])
        x = responder("rating", questions["rating"])
        print(x)

def sender(content):
    print(content)

def loopMorning():
    sender("goals")
    intent = responder("goals")
    sender("sleep")
    sleep = responder("sleep")
    sender("rating")
    rating = responder("rating")
    quote()

def loopNoon():
    sender("midday")
    midday = responder("midday")
    sender("eating")
    eat = responder("eating")
    sender("rating")
    rating = responder("rating")
    quote()
def evening():
    sender("interact")
    interact = responder("interact")
    sender("")


def loopNight():
    sender("future")

def loopReflection():
    sender()

def quote():
    print("whales are the largest animals on earth")

questions = {
    "rating": "Rate how you're feeling from a scale of 1 to 10",
    "midday": "Anything noteworthy happen in your day so far?", 
    "sleep": "Rate your quality of sleep on a scale of 1 to 10",
    "advice": "what is some advice you would give to someone in your situation",
    "goals": "What are your goals for the day",
    "cause": "What happened to ",
    "grateful": "What are you grateful for today?",
    "productive": "Have you been productive thus far in your day?",
    "eating": "What did you eat?",
    "interact": "Who did you interact with today and how did it make you feel?",
    "new": "Did you experience anything new today?",
    "goodThings": "What is something good you did today?",
    "future": "What can you do later in the week that can help yopu be more productive?",
    "feelings": "How did you feel after a negative event this week?",
    "selfadvice": "What advice would you give to someone else in your situation?",
    "nofilter": "What is something you would want to tell that person that you havent?"
}


