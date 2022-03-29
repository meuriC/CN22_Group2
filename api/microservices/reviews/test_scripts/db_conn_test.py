from bson.objectid import ObjectId  
from pymongo import MongoClient
import pymongo

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@reviews.kqme2.mongodb.net/test"

    # Create a connection using MongoClient. 
    client = MongoClient(CONNECTION_STRING)

    return client['database']
    

if __name__ == "__main__": 
    # Get the database
    dbname = get_database()
	
    collection_name = dbname['reviews']
    #item_details = collection_name.find({"_id": ObjectId("62410a9b8b3c1792b732e1e0")}) # IT WORKS
    #item_details = collection_name.find({"review_id": "50463082"})  # IT WORKS
    item_details = collection_name.find({"app_id": {"$all": ["883710"]} }).limit(3)  # IT WORKS
	
    for item in item_details:
       print(item)