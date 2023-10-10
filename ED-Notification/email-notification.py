from email.message import EmailMessage
import smtplib
import json
import time

file_path = '/Users/maclarsen/cs/email_trial/mockDB.json'

with open(file_path, 'r') as openfile:
    data = json.load(openfile)

def send_email(objects):
    sender = 'mistered.health@gmail.com'
    password = 'xquy owpn pqqe ctis'
    receiver = objects['email']

    subject = 'Mister Ed: Queue Update'
    body = objects['name']+", you are next to receive treatment at " + objects['nearestED'] + ". Please travel there now."

    time.sleep(objects['wait'])

    message = EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, message.as_string())
