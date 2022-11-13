import datetime
import time as t
import sendnreceive as sms

def dailyRoutine():
    while 1:
        time = str(datetime.datetime.now())[10:15]
        checkTime(time)
        t.sleep(20)
        
        #question types ratings, reminder, yn
def responder(clock):
    sms.checkMsg(clock)
    f = open("test.txt", "a")
    response = input()
    f.write(response)
    f.close()

def quote():
    print("whales are the largest animals on earth")
def sender(content):
    sms.sendMsg(questions[content])


def checkTime(time):
    if time == "09:0":
        loopMorning()
    elif time == "01:0":
        loopNoon()
    elif  time == "18:0":
        loopEvening()
    elif time == "22:0":
        loopNight()
    else:
        loopTest()

def loopMorning():
    sender("goals")
    sender("sleep")
    sender("rating")
    responder(datetime.datetime.now())
    quote()

def loopNoon():
    sender("productive")
    sender("eating")
    sender("rating")
    responder(datetime.datetime.now())
    quote()
def loopEvening():
    sender("interact")
    sender("midday")
    sender("rating")
    responder(datetime.datetime.now())
    quote()
def loopNight():
    sender("future")
    sender("feeling")
    sender("rating")
    responder(datetime.datetime.now())
    quote()
def loopReflection():
    sender("grateful")
    sender("interact")
    sender("advice")
    responder(datetime.datetime.now())
    quote()
def loopTest():
    quote()
    sender("dreams")
    sender("advice")
    sender("nofilter")
    sender("rating")
    responder(datetime.datetime.now())
    quote()
def report():
    print("report")


questions = {
    "rating": "Rate how you're feeling from a scale of 1 to 10",
    "midday": "Anything noteworthy happen in your day?",
    "sleep": "Rate your quality of sleep on a scale of 1 to 10",
    "dreams": "Did you have any dreams?",
    "advice": "What is some advice you would give to someone in your situation?",
    "goals": "What are your goals for the day",
    "cause": "What happened to ",
    "grateful": "What are you grateful for today?",
    "productive": "Have you been productive thus far in your day?",
    "eating": "What did you eat?",
    "interact": "Who did you interact with today?",
    "feeling": "How did they ",
    "new": "Did you experience anything new today?",
    "goodThings": "What is something good you did today?",
    "future": "What can you do later in the week that can help yopu be more productive?",
    "feelings": "How did you feel after a negative event this week?",
    "selfadvice": "What advice would you give to someone else in your situation?",
    "nofilter": "What is something you would want to tell that person that you havent?"
}


