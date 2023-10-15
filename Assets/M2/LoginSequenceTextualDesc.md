## Sequence Diagram: Login Sequence

### Description:
The Login Sequence Diagram demonstrates the exchange of messages between the User,
UI, Authentication Server, and Database.

### Participants:
- **User**: The User is a person that is eligible to recieve medical care in BC that is registered with MSP and has a Personal Health Number (PHN).
- **User Interface (UI)**: Represented the web based interface for the User to access the system.
- **Authentication Server (Auth)**: A 3rd party authentication service hosted by BC Gov that allows the system to authenticate a user for access to the system based on both valid credentials, and medical care eligibility.
- **Database (DB)**: Stores user session data for interaction with the system as provided by the authentication provide and the user.

### Messages:
1. **User Credentials**: User submitted PHN and passphrase provided in web UI.
2. **Token Exchange**: UI forwards user credentials as OAuth request to 3rd part Authentication server and stores valid response token for session in DB
3. **Valid Reponse Token**: Returned from 3rd party Authentication server, and directed to UI to update user view to Emergency Department (ED) Map view.
4. **Invalid Response Token**: Returned from 3rd party Authentication server, and directed to UI to update user view to have client re-attempt login request.

### Notes:
- **Authentication Fragment (Messages: Step 2)**: Refer to Registeration Sequence Diagram for a description of the Authentication Fragment
