import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/gagarin_db')
client = MongoClient(mongo_uri)
db = client.get_database()
