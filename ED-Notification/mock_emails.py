from email.message import EmailMessage
import json
from email_notification import send_email

file_path = '/Users/maclarsen/cs/email_trial/mockDB.json'

with open(file_path, 'r') as openfile:
    data = json.load(openfile)

def main():
    for objects in data:
        send_email(objects)

if __name__ == "__main__":
    main()
