from app.utils.db import db
class Entry:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password 

    def to_dict(self):
        return{
            "name" : self.name,
            "email" : self.email,
            "password" : self.password
        }
