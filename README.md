TODO: Continually update as project evolve.

# README

## How to create diagrams

Navigate to [https://app.diagrams.net/?mode=github](https://app.diagrams.net/?mode=github) and authorize with your GitHub.

### Existing Document

Select Existing Document and scroll down to uvic-teach/project-m1-team9, navigate to /Assets/ and begin editing a file. Save at the top when changes are complete and changes will be commited to repo.

### New Document

Select new document. Changes file type to png so that you can link directly to it in Markdown files and they render instantly.

# Feature Contribution

Create a new branch with a descriptive lowercase name in your preferred Git interface (GUI, CLI, etc.)
Commit any diagrams in relation to your feature branch in /Assets/ per the [how-to-create-diagrams](https://github.com/uvic-teach/project-m1-team9/tree/main#how-to-create-diagrams) section above.
Create pull request when you wish to merge your feature into main - add comments if necessary and have it review by one other person on the team.

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