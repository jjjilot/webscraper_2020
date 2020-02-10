from twilio.rest import Client
from output_variables import *
from datetime import time
from datetime import datetime

client = Client(account_sid, auth_token)
# client.messages.create(body="test text",to=my_phone_number,from_=twilio_phone_number)

now = datetime.now()
dt_string = now.strftime("%H:%M")
dt_hour = now.strftime("%H")
if int(dt_hour)<12:
    am_pm = 'in the morning'
else:
    am_pm = 'in the afternoon'
message = 'The current time is ' + str(dt_string) + ' ' + am_pm + '.'

def send_text():
    # message_to_send = str(input('Message to send: '))
    client.messages.create(body=message,to=my_phone_number,from_=twilio_phone_number)

send_text()