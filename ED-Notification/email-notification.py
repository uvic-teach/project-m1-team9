import os
from email.message import EmailMessage
import smtplib
import json

file_path = '/Users/maclarsen/cs/email_trial/mockDB.json'

with open(file_path, 'r') as openfile:
    data = json.load(openfile)

specific_object = data[0]

sender = 'mistered.health@gmail.com'
password = 'xquy owpn pqqe ctis'
receiver = specific_object['email']

subject = 'Mister Ed: Queue Update'
body = specific_object['name']+", you are next to receive treatment at " + specific_object['nearestED'] + ". Please travel there now."

message = EmailMessage()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.set_content(body)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, message.as_string())
