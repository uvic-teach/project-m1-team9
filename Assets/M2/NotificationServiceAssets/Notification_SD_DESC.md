## SD-6: Register to Mr ED

### Description:
The notification sequence diagram represents the process of sending a notification once the user has completed virtual triage with the Mr ED system.  This includes interaction with a 3rd party email service.

### Participants:
- Patient: The Mr ED user who has completed virtual triage and is waiting for their turn to travel to travel to an ED.
- Virtual Triage Microservice: The Mr ED microservice responsible for completing the virtual triage with the user and determining their results.
- Notification Microservice: The Mr ED microservice responsible for notifying the user when it is their turn to go to an ED.
- ED Load Microservice: The Mr ED microservice responsible for determining and displaying the queue loads at a given ED. 
- ED: The health care facility the user will be travelling to when it is their turn to receive treatment.
- Google Email Service: The email service which delivers the notifications via email to the user.
 
### Messages:
1. Once virtual triage is completed, user agrees to receive a notification
2. Virtual Triage Microservice requests that a notification be sent to user
3. A loop occurs while there is a queue for the ED
1. Notification Microservice requests the ED load
2. ED Load Microservice requests the ED load
3. ED returns the queue load 
4. ED Load Microservice returns the queue load
5. Notification Microservice requests an email be sent to the user
6. Google Email service sends the email notification to the patient and makes the sent email viewable to the Notification Microservice.
