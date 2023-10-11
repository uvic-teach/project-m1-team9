from email.message import EmailMessage
import smtplib
import json
import time

with open('mockDB.json', 'r') as openfile:        #access json file and saves objects as list to data
    data = json.load(openfile)

def send_email(objects):
    sender = 'mistered.health@gmail.com'  #address email sent from
    password = 'xquy owpn pqqe ctis'      #password to send fro above address
    receiver = objects['email']           #address of recipient (taken from json for mock or INSERT YOUR EMAIL HERE TO VIEW RESULTS FOR MARKING PURPOSES)

    subject = 'Mister Ed: Queue Update'        #email subject header
    body = objects['name']+", you are next to receive treatment at " + objects['nearestED'] + ". Please travel there now."        #email body

    #time.sleep(objects['wait'])        #Pause to mimic receiving queue update from ED (time taken from json for mock)

    message = EmailMessage()
    message['From'] = sender   
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, message.as_string())
