import pymongo
from pymongo import MongoClient
import os

secret = os.environ.get("DB_PASS")

cluster = pymongo.MongoClient(f"mongodb+srv://azuniga:{secret}@cluster0.oykhk.mongodb.net/pymongo_auth?retryWrites=true&w=majority")
db = cluster["pymongo_auth"]
collection = db["users"]

def add_user(user):
    return collection.insert_one(user)

def check_for_user(email):
    if collection.find_one({"email" : email}):
        return True
    else:
        return False
    
# def delete_user(user):
#     pass
    
# def update_user(user):
    

