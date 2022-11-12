# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACc660c8106da96416f43facdc03092be5"
auth_token = "a4ae8cb91b569ca32d85ed8f08859af1"
client = Client(account_sid, auth_token)

public_key = client.accounts \
                   .v1 \
                   .credentials \
                   .public_key \
                   .create(public_key='publickey')

print(public_key.sid)