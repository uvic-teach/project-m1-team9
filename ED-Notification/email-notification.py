import os
from email.message import EmailMessage
import smtplib
import json

with open('mockDB.json', 'r') as openfile:
    json_object = json.load(openfile)

specific_object = data[0]

sender = 'mistered.health@gmail.com'
password = 'xquy owpn pqqe ctis'
receiver = specific_object[1]

subject = 'Mister Ed: Queue Update'
body = specific_object[0]+"You are next to receive treatment at" + spcific_object[2] + ". Please travel there now."

message = EmailMessage()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.set_content(body)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, message.as_string())
