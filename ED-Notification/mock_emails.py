from email.message import EmailMessage
import json
from email_notification import send_email

with open('mockDB.json', 'r') as openfile:;        #open json file and save objects to data as list
    data = json.load(openfile)

def main():
    for objects in data:
        time.sleep(30)
        send_email(objects)

if __name__ == "__main__":
    main()
