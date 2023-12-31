# Mr. ED

![badge](https://github.com/uvic-teach/project-m1-team9/actions/workflows/mred.yml/badge.svg)

A Django based user interface for the Mr. ED project. Acts as a bridge for the user to access all microservices.

Hosted on Google Cloud. Visit [here](https://mr-ed-dot-extreme-lodge-401820.wl.r.appspot.com/mred/)!

The microservices incorporated are:
- User Management Microservice
- Notifications Microservice
- ED Maps Microservice

Each microservice has their own directory, and associated README.

## Feature Contribution

The current workflow is to maintain a "dev" branch and a "main" (production) branch. Main should not be touched until milestone completion, where all work from the dev branch will be merged in.

To develop a feature, create a new branch with a descriptive lowercase name in your preferred Git interface (GUI, CLI, etc.). Commit any code changes into the feature branch. For associated diagrams, commit them the dev branch, NOT the feature branch.

Create pull request when the feature is complete, to merge your feature into dev - add comments if necessary and have it review by one other person on the team. Afterwards, close the feature branch.

At the end of the milestone / sprint, dev will be merged into main. We have dev as the "default" branch to avoid accidentally branching from or adding to main, so to merge dev into main, main will have to be swapped back into being the default branch.

## How to create diagrams

Navigate to [https://app.diagrams.net/?mode=github](https://app.diagrams.net/?mode=github) and authorize with your GitHub.

### Existing Document

Select Existing Document and scroll down to uvic-teach/project-m1-team9, navigate to /Assets/ and begin editing a file. Save at the top when changes are complete and changes will be commited to repo.

### New Document

Select new document. Changes file type to png so that you can link directly to it in Markdown files and they render instantly.

## EDMapService

![edmapservice-ci](https://github.com/uvic-teach/project-m1-team9/actions/workflows/edmapservice.yml/badge.svg)

A microservice designed to display a map of nearby Emergency Departments based on the user's location. Automatically integrated via workflows and deployed to Google Cloud. Visit the live development version [here](https://edmapservice-dot-extreme-lodge-401820.wl.r.appspot.com/edmap/)!

## How to contribute to the EDUserManagement Service

1. Clone the repository and navigate to the project directory - you should see ```manage.py```.

2. Create a Virtual Environment:

   - To create a virtual environment, use the following command:

     ```bash
     python3 -m venv venv
     ```

     Replace `venv` with your preferred name for the virtual environment.

   - **Activate the Virtual Environment**:

     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

     - On macOS and Linux:

       ```bash
       source venv/bin/activate
       ```

   Using a virtual environment is recommended to isolate project dependencies, and avoid you filling your default python3 install with a lot of packages.

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
4. Build/Update database schema
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
5. Run the server
    ```bash
    python3 manage.py runserver
    ```
    Open your web browser and visit http://localhost:8000 to see the project running.

6. Make a curl request to check an endpoint
    ```bash
    curl http://localhost:8000/eduser/user/1/

### Testing Service Tokens with the Application

To contribute to this application and test service tokens, follow these concise steps:

1. **Generate a Service Token:**
   - Use the Django admin panel or Django shell to generate a token for your service. 
   - For Django shell:
     ```bash
     python manage.py shell
     ```
     Then in the shell:
     ```python
     from EDUserManagementApp.models import ServiceAccount
     ServiceAccount.objects.create(service_name='YourServiceName', token='your_generated_token')
     ```

2. **Start the Django Development Server:**
   - Run the Django development server:
     ```bash
     python manage.py runserver
     ```

3. **Make a `curl` Request:**
   - Use `curl` to make a request to the application, including the service token in the request header.
   - Replace `your_generated_token` with the token from step 1 and `your_endpoint` with the specific endpoint you wish to test:
     ```bash
     curl -H "Authorization: your_generated_token" http://localhost:8000/your_endpoint/
     ```

4. **Analyze the Response:**
   - A successful response indicates that the service token is working.
   - An unauthorized error (status code 401) indicates an invalid or missing token.

Please ensure your service name and generated token are kept secure and are used in accordance with our application's security guidelines.

TODO: In the future we will need to setup repository secrets with unique keys for each service, and inject them into the application during the GitHub Actions
workflow for each microservice.