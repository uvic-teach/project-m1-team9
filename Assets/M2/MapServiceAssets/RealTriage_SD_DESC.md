## Sequence Diagram: Real Triage Sequence

### Description:
The Real Triage Sequence Diagram demonstrates how a user would be directed to visit an Emergency Department (ED) for an in-person triage.

### Participants:
- **User**: The User is a person that is eligible to recieve medical care in BC that is registered with MSP and has a Personal Health Number (PHN).
- **User Interface (UI)**: Represented the Mister ED web based interface for the User to access the system.
- **Emergency Department (ED)**: Emergency Department that recieves the user for an in-person triage with intent of assuming responsibility of care for the user afterwards.
- **Database (DB)**: Stores user appointment and ED schedule data to orchestrate when the user is to visit the ED in person.

### Messages:
1. **Take virtual triage**: User accepts a virtual triage on the Mister ED interface.
2. **Make ED appointment**: UI forwards user credentials and virtual triage results to the DB for scheduling a visit to an ED.
3. **Make in-person triage appointment**: UI forwards user credentials and the failed virtual triage results to the DB for an in-person triage appointment with an ED.
4. **Notify of appointment**: DB notifies the Emergency Department that an appointment with a user was successfully scheduled, with details on whether it is for an in-person triage or for post-triage care.
5. **Appointment made**: DB notifies the user interface that an in-person triage or post-triage care appointment has been successfully scheduled, with details on location and time.
6. **Appointment information**: User interface displays to the user that an appointment has been successfully made, with details on the ED location, and time.
