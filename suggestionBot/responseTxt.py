from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse, Message
app = Flask(__name__)




@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")
    return str(resp)

if __name__ == '__main__':
   app.run(debug=True)
