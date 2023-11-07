from email.message import EmailMessage
import json
from email_notification import EmailFactory
import time

##########################################################################

#run this python file to test/mock email_notification.py
#this program will take up to around an entire minute to for all emails to be sent and will continue to run until manually terminated

#ensure that <INSERT YOUR EMAIL> in this file and in mockDB.json 
#are changed to the email address that you want this message sent to

##########################################################################

file_path = "mockDB.json"

with open('mockDB.json', 'r') as openfile:;        #open json file and save objects to data as list
    data = json.load(openfile)

def main():

#i = 0                     ###Uncomment to add a user while the program is running, uncomment the commented code below as well
    
    while True:
        
        with open(file_path, 'r') as openfile:  #read json file (in loop as new users may be added while running)
            data = json.load(openfile)
            
        for objects in data:        #iterates through each user
            email_factory.send_email(sender = 'mistered.health@gmail.com', password = 'xquy owpn pqqe ctis', receiver = objects['email'], subject = 'Mister Ed: Queue Update', body = objects['name'] + ", you are next to receive treatment at " + objects['nearestED'] + ".\nPlease travel there now.")
     #calls email function from file
           
            if(objects['EDqueue']>=0):    
                objects['EDqueue'] = objects['EDqueue']-1  #moves user up queue as long as they arent already at the front
        
        time.sleep(1) #slows down mock to determine incoming email order
        
                                                ###Uncomment below to add a user while the program is running###
        #i = i+1
        #if i==10:
        #    data.append({"name": "Mary", "email": "<INSERT YOUR EMAIL HERE>", "nearestED": "Oak Bay Urgent Care Clinic", "EDqueue": 10})
        #   with open(file_path, 'w') as openfile:
        #        json.dump(data, openfile)
        
        with open(file_path, 'w') as openfile:  #update json file (in loop as new users may be added while running
            json.dump(data, openfile)
            
        time.sleep(1) #slows down mock to determine incoming email order and ensure that JSON is not empty following mock

if __name__ == "__main__":
    main()
