  
import twilio

from twilio.rest import Client
account_sid = 'your account sid'
auth_token = 'your auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='Message to send',
         from_='sender number with country code',
         to='receiver number with country code'
     )

print(message.sid)
