## Deployment Diagram

### Description:
This deployment diagram shows that we're planning on using a docker to host our python scripts and user data.

### Nodes:
- emails.py
  - Links email_notification.py and the User DB together to send emails to the users as they come off of the queue.
- email_notification.py
  - Defines the email notification sent. The text inside and the structure of the email.
- User DB
  - Holds the user objects and the queue that we update as the ED's update their queues.

- [Other Microservices]:
  - Gmail
    - Utilized to send the emails for us through the misterED email account using their platform.

#### Notes:
1. Queue implementation must be closely linked to how it is set up in the ED's.
2. Userdata that is stored must be secured and not tampered with. No excessive data and we must protect user confidentiality where possible.
