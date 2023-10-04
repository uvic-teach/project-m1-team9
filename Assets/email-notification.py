import os
from email.message import EmailMessage
import smtplib

sender = 'mistered.health@gmail.com'
password = 'xquy owpn pqqe ctis'
receiver = 'larmac2019@gmail.com'

subject = 'Mister Ed: Queue Update'
body = "You are next to receive treatment at the Victoria General Hospital Emergency Department. Please travel there now."

message = EmailMessage()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.set_content(body)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, message.as_string())
