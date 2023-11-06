from email.message import EmailMessage
import json
from email_notification import send_email

file_path = "mockDB.json"

with open('mockDB.json', 'r') as openfile:;        #open json file and save objects to data as list
    data = json.load(openfile)

def main():
    while(1):
        with open(file_path, 'r') as openfile:  #read json file (in loop as new users may be added while running)
            data = json.load(openfile)
        for objects in data:        #iterates through each user
            send_email(objects)     #calls email function from file
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
