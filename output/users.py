from pymongo import MongoClient
from bson.json_util import dumps

# Connect to the database
client = MongoClient("mongodb://localhost/emotions")

def getCompanyWithName(name):
    emotions = client.get_default_database()["users"]
    query = emotions.find_one({"name": name})
    if not query:
        raise ValueError("Company not found")
    return dumps(query)