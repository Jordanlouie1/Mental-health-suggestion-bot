import twilio
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import time
import datetime

ssid = input('Enter Twilio SSID: ')
authcode = input('Enter Auth Code from Twilio: ')
number = int(input('Enter Twilio number: '))
to = input('Number to send: ')
ssid = "AC9b02dd7d84972e0b115182baab1368ec"
authcode = "d2f5f2f207e6da5562bde1fd1c4cf50e"
number = "+18176314549"

client = Client(ssid, authcode)
length = len(client.messages.list())
def sendMsg(message):
    client.messages.create(to=to,
                       from_=number,
                       body=message)
    time.sleep(8)
    length = len(client.messages.list())
    while length == len(client.messages.list()):
        time.sleep(5) #waiting for message

def checkMsg(clock):
    msgs = client.messages.list()
    f = open("response.csv", "a")
    for msg in msgs:
        if (msg.direction == 'inbound'):
            f.write(str(datetime.datetime.now()) + ', ' + msg.body + ', \n')
    f.write('\n ')
    f.close()


