## User Management Component Diagram Description

### Description

### Ports

#### ManageUsers
The User Management microservice supplies a ManageUsers interface that gives access to user data, and user registration functionality.  This interface is structured as a REST API.

#### DB Access
The User Management microservice depends on access to a database.  This database is soley accessed by the user management microservice.  This access is abstracted through an interface to lower the dependancy on the particular DB schema being used.

### Sub Components

#### User Repository
##### Description
This component further abstracts access to the database by providing specific user queries.
##### Provides
- User repository
##### Dependencies
- Access to user database

#### User Service
##### Description
Impliments business logic, and provides abstracted functionality needed for REST API endpoint requests.
##### Provides
- User service
##### Dependencies
- User repository
- User registration

#### User Registration
##### Description
A component that is responsible for user registration logic.  This component is necesary to decrease dependancy on some specific registration strategy (what data is required, how auth is handled, etc...).
##### Provides
- User registration logic
##### Dependencies
- None

#### User Controller
##### Description
A component that handles REST API routes. This component will be responsible for responding to requests.
##### Provides
- User controller
##### Dependencies
- User service
