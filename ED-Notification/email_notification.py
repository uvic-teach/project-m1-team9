from email.message import EmailMessage
import smtplib
import json

file_path = "mockDB.json"

with open(file_path, 'r') as openfile:
    data = json.load(openfile)

def send_email(objects):

    if(objects['EDqueue'] == 0):

        sender = 'mistered.health@gmail.com'  #email is sent from
        password = 'xquy owpn pqqe ctis'  #password needed to access gmail to send email
        receiver = objects['email']  #recipient of email (taken from json for mock)

        subject = 'Mister Ed: Queue Update' #subject of email
        body = objects['name']+", you are next to receive treatment at " + objects['nearestED'] + ".\nPlease travel there now." #mail script

        message = EmailMessage()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject
        message.set_content(body)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, message.as_string())
