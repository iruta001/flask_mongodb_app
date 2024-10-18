from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client['userinfo_db']
    print('Mongodb connected sucessfully')
except Exception as e:
    print(f'Mongodb failed to connect:{e}')
