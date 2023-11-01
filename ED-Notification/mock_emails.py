from email.message import EmailMessage
import json
from email_notification import send_email

file_path = "mockDB.json"

with open('mockDB.json', 'r') as openfile:;        #open json file and save objects to data as list
    data = json.load(openfile)

def main():
    while(1):
        for objects in data:
            send_email(objects)
            if(objects['EDqueue']>=0):
                objects['EDqueue'] = objects['EDqueue']-1

if __name__ == "__main__":
    main()
