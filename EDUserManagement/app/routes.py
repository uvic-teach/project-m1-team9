from run import app
from flask import jsonify
from app.models import User  # Import your User model
from flask import current_app

@app.before_request
def init_dummy_data():
    dummy_data = current_app.dummy_data

@app.route('/check_app')
def check_app():
    return f"App ID in routes.py: {id(current_app._get_current_object())}"

# Make sure to load your dummy_data somewhere before this
# For example, in your create_app function or __init__.py
# dummy_data = ...
@app.route('/test')
def test():
    print("This route is running")
    return "This is a test."

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    # Assume that dummy_data is either imported or accessible through current_app
    print(f"Searching for user with ID: {user_id}")
    user = User.find_by_id(user_id, current_app.dummy_data)  # Using the new method in your User class
    print(f"Found user: {user}")
    if user:
        # Convert the user object to a dictionary to jsonify it
        user_dict = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        }
        return jsonify(user_dict), 200
    else:
        return jsonify({'message': 'User not found'}), 404
