from twilio.rest import Client
from output_variables import *

client = Client(account_sid, auth_token)
client.messages.create(body="test text",to=my_phone_number,from_=twilio_phone_number)
