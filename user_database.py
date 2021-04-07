import pymongo
from pymongo import MongoClient
import os

user = os.environ.get("DB_USER")
secret = os.environ.get("DB_PASS")

cluster = pymongo.MongoClient(f"mongodb+srv://{user}:{secret}@cluster0.oykhk.mongodb.net/pymongo_auth?retryWrites=true&w=majority")
db = cluster["pymongo_auth"]
collection = db["users"]

def add_user(user):
    return collection.insert_one(user)

def check_for_user(email):
    if collection.find_one({"email" : email}):
        return True
    else:
        return False
    
def get_user(email):
    return collection.find_one({"email" : email})
    
# def delete_user(user):
#     pass
    
# def update_user(user):
    

