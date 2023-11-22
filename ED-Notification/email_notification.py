from email.message import EmailMessage
import smtplib
import json
import socket

class EmailFactory:
    def create_email(self, sender, password, receiver, subject, body):
        message = EmailMessage()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject
        message.set_content(body)
        return message

    def send_email(self, sender, password, receiver, subject, body):
        message = self.create_email(sender, password, receiver, subject, body)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, message.as_string())


def pollTheED(s, name):

    # Package out the string and send it across the socket
    #package = json.dumps({"name": name})
    s.send(name.encode())

    # Wait for a response from the ED
    recieved_data = s.recv(1024).decode()
    #recieved_data = json.loads(recieved_data.decode())

    return recieved_data #recieved_data.get("should_send_notif")

def main():

    # Setup & config socket for ED communication as client
    s = socket.socket()
    s.setblocking(1) # important
    host = socket.gethostname()
    port = 9981
    s.connect((host, port))
    #s.setblocking(1) # important

	#def send_email(objects):

    while True:

		# Open the database for the users waiting for a notification
        file_path = "mockDB.json"
        with open(file_path, 'r') as openfile:
            data = json.load(openfile)
		# M4 todo: shouldn't there be a 'close file' somewhere?
		
		# Loop through each person awaiting a notification:
        for user in data:
    
            # Poll the Ed once (final return val is string = "True" or = "False")
            pollresult = pollTheED(s, user['name'])

            if(pollresult == "True"):
    
                print("Time to send an email! To " + user['name'])

                sender = 'mistered.health@gmail.com'  #email is sent from
                password = 'xquy owpn pqqe ctis'  #password needed to access gmail to send email
                receiver = user['email']  #recipient of email (taken from json for mock)
                subject = 'Mister Ed: Queue Update' #subject of email
                body = user['name']+", you are next to receive treatment at " + user['nearestED'] + ".\nPlease travel there now." #mail script
    
                email_factory = EmailFactory()
                email_factory.send_email(sender, password, receiver, subject, body)		

if __name__ == "__main__":
    main()
