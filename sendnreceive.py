import twilio
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import time
import datetime

ssid = input('Enter Twilio SSID: ')
authcode = input('Enter Auth Code from Twilio: ')
number = int(input('Enter Twilio number: '))

ssid = "AC9b02dd7d84972e0b115182baab1368ec"
authcode = "911070b8c4689bf8ad7ad1eeaaecda7c"
number = "+18176314549"

client = Client(ssid, authcode)

def sendMsg():
    to = input('Number to send: ')
    message = input('Message: ')

    client.messages.create(to=to,
                       from_=number,
                       body=message)

def checkMsg():
    msgs = client.messages.list()
                      #date_sent_after=datetime(2022, 1, 15, 1, 23, 45),
                      #date_sent_before=datetime(2022, 1, 17, 1, 23, 45),
                      #limit=20)
    for msg in msgs:
        if (msg.direction == 'inbound'):
            print(str(datetime.datetime.now()) + ', ' + msg.body + ', ')


