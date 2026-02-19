

class User:

    _id_counter = 1000
    def __init__(self, username, email, password):
        User._id_counter += 1
        self.id = User._id_counter
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

