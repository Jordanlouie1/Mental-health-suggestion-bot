from sendnreceive.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACa4138a01aabf0ec2d44a1b52fc8b8e2b"
auth_token = "ee8aaff667478866598fb420d405ec80"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="What's your mood for today?",
                     from_='+19856025576',
                     to='+16179490767'
                 )

print(message.sid)
