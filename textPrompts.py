import datetime

def dailyRoutine():
    print('hello')
    print(datetime.datetime.now())

#question types ratings, reminder, yn
def responder(qtype, response):
    if qtype == 'rating':
        print(response)
    if qtype == 'dialog':
        print(response)
    if qtype == 'yn':
        print(response)


