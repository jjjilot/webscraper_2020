from twilio.rest import Client
from output_variables import *
from datetime import time
from datetime import datetime

def send_text(website_url, line_of_discrepancy):
    client = Client(account_sid, auth_token)
    now = datetime.now()
    dt_string = now.strftime("%I:%M")
    dt_hour = now.strftime("%H")
    if int(dt_hour)<12:
        am_pm = 'in the morning'
    else:
      am_pm = 'in the afternoon'
    message = 'Discrepancy found at ' + website_url + ' on line ' + str(line_of_discrepancy) + ' at ' + str(dt_string) + ' ' + am_pm + '.'
    client.messages.create(body=message,to=my_phone_number,from_=twilio_phone_number)

send_text('www.csmoodle.clevelandhighschool.org', 12)

