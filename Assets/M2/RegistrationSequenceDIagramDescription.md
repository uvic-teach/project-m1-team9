## SD-5: Register to Mr ED

### Description:
The registration sequence diagram represents the process of registering a new users with the Mr ED system.  This includes interaction with a 3rd part authentication provider.

### Participants:
- User: The Mr ED user who is registering with Mr ED.
- UI: The interface through which the user is interacting with the Mr ED system.
- Auth Provider: A provider of user auth. This provider is being treated as a black box. In practice, this would be some private, or governent related system that verifies user credentials (PHN, name) and manages auth.
- User Management: The Mr ED server responsible for persisting user data. 

### Messages:
1. User enters their name
2. User enters their personal health number (PHN)
3. User enters their date of birth
4. User enters their password
5. Register with auth provider: the users password, PHN and name is sent to an auth provider.
6. Valid registration
    1. User token: the auth provider returns some unique identifier that can be used to associate the users data with their authentication credentials.
    2. User registration: user token, along with user registration form details are sent to the Mr ED user management service to be persisted.
6. Invalid registration
    1. Notify invalid: The auth provider notifies the UI that the provided registration credentials are invalid
    2. Prompt to try again: The UI displays a message to the user, indicating that they must try entering different credentials

### Authentication fragment

#### Participants:
- User
- UI
- Auth provider

#### Messages:
1. PHN and Password: The users authentication credentials are sent to the auth provider
2. JWT and User Token: A JWT and user token are returned to the UI - the JWT will manage the users authenticated session, and the user token will be used to determine what details are needed from the Mr ED user management system.
3. User token sent to Mr ED user management: The users token is sent to Mr ED, and any necessary data for the users session is returned.
