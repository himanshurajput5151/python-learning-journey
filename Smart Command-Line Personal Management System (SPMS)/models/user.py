import uuid

class User:


    def __init__(self, username, email, password):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'user_id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'password' : self.password
        }

