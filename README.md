# Twilio-sms-api
# First:
You need to create an account on Twilio with your email and 14 digit password, after that it demands your mobile number then you’ll get an OTP on your device.
login in Twilio with your email id and 14 digit password it’ll ask you to generate a free trial number you can choose and generate it or you can purchase its services.
# Second: 
Twilio provide account_session_id and auth_token that interact with python, which is going to use in our code.
# Third: 
For python, you need to install twilio, you can do this by using
pip install twilio
# Fourth: 
From twilio get your account_sid and auth_token which is used by twilio Client module like:
client = Client(account_sid, auth_token)
# Fifth: now you write python code and type your message in the body section and run the code. it will provide you a massage session-id which indicates that message successfully sent to the user mobile number.
