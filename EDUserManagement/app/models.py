from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User:
    def __init__(self, id, username, email, password, created_at, updated_at):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def get_dummy_users(cls, dummy_data):
        # Create User objects based on the dummy data
        return [cls(**data) for data in dummy_data]

    @classmethod
    def find_by_id(cls, user_id, dummy_data):
        # Find and return a user by their ID
        user_data = next((item for item in dummy_data if item['id'] == user_id), None)
        if user_data:
            return cls(**user_data)
        return None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'