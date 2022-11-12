import os
from twilio.rest import Client
import json

# Find your Account SID at twilio.com/console
# Provision API Keys at twilio.com/console/runtime/api-keys
# and set the environment variables. See http://twil.io/secure
account_sid = "ACa4138a01aabf0ec2d44a1b52fc8b8e2b"
auth_token = "ee8aaff667478866598fb420d405ec80"
client = Client(account_sid, auth_token)

message = client.messages('SM01b97f441b48cf0f4c23476a4e7b7b73').fetch()
print(message.to)
