from flask import Flask
from flask_bcrypt import Bcrypt
import json

def create_app():
    app = Flask(__name__)
    Bcrypt(app)

    # Load the JSON data from the file
    with open('app/dummy_users.json', 'r') as file:
        dummy_data = json.load(file)

    app.dummy_data = dummy_data  # Attach to app instance
    return app


