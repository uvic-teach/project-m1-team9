from email.message import EmailMessage
import json
from email_notification import EmailFactory


file_path = "mockDB.json"

def main():
    
    while True:
        
        with open(file_path, 'r') as openfile:  #read json file (in loop as new users may be added while running)
            data = json.load(openfile)
            
        for objects in data:        #iterates through each user
			# @Mac this is undefined, you fool
            email_factory.send_email(sender = 'mistered.health@gmail.com', password = 'xquy owpn pqqe ctis', receiver = objects['email'], subject = 'Mister Ed: Queue Update', body = objects['name'] + ", you are next to receive treatment at " + objects['nearestED'] + ".\nPlease travel there now.")
     #calls email function from file


if __name__ == "__main__":
    main()
