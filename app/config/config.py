import os

class config:
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')