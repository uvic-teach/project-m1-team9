## Deployment Diagram: Map_DD

### Description:
Outlines the MapService Deployment Diagram, which involves deployment of the EDMapService microservice to Google Cloud servers.

### Nodes:
- GitHub CI/CD Machine: A virtual machine managed by GitHub that runs the CI/CD scripts for the Django webapp.
- Google Cloud: A cloud service provider, with built-in management for scaling, APIs, storage, and more.
- EDMap Service App Engine: An environment which the Django application runs on in the Google Cloud servers.

### Components:
- Web Server: The running production version of the EDMapService Django webapp
- User Device: The machine users utilize to connect to the web server via a web browser or the MrED User interface.
- Cloud storage: Storage in the Google Cloud servers that is dedicated for the App Engine's static files, images, Django files, etc.

### Artifacts:
- `app.yaml`: A configuration file used by the Google Cloud App Engine to configure the deployment environment.
- Google Cloud credentials: A secret variable holding the authentification credentials to the accompanying Google Cloud project.

### Dependencies:
1. The Google Cloud CLI depends on `app.yaml` and the Google Cloud credentials variable in order to properly target and set up the desired App Engine.
2. The App Engine depends on Cloud storage for runtime files, and on Google Cloud for resource management and traffic routing.
3. The GitHub CI/CD Machine depends on GitHub management and servers in order to execute the appropriate CLI scripts to activate the Google Cloud deployment.

### Communication Paths:
- GCloud CLI: The GitHub CI/CD Machine utilizes the Google Cloud CLI to invoke an App Engine deployment on their servers of the specified application in the repository.
- HTTPS Request: The user accesses the live web server via secure HTTPS requests on Google Cloud's App Engine. 
