from bson.objectid import ObjectId  
from pymongo import MongoClient
import pymongo
#import time

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@reviews.kqme2.mongodb.net/test"
    #CONNECTION_STRING_3 = "mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@reviews3.keyxx.mongodb.net/test"

    # Create a connection using MongoClient. 
    client = MongoClient(CONNECTION_STRING)

    return client['database']
    

if __name__ == "__main__": 
    # Get the database
    dbname = get_database()
	
    collection_name = dbname['reviews']
    #item_details = collection_name.find({"_id": ObjectId("62410a9b8b3c1792b732e1e0")}) # IT WORKS
    item_details = collection_name.find({"author": {"steamid": "76561198054155096"}  })  # IT WORKS
    #item_details = collection_name.find({"app_id": {"$all": ["883710"]}, "language": {"$all": ["english"]} }).limit(3)  # IT WORKS   
	
    """item_details = collection_name.find({"review_id": "test"})
	
    collection_name.update_one({"review_id": "test"}, {"$set": {"review": "This is a test review by yours truly ren ::sad_face::"}}, upsert=True)
    collection_name.update_one({"review_id": "test"}, {"$set": {"recommended": "False"}}, upsert=True)"""
	
    #epoch_time = int(time.time())
    #print(epoch_time)
	
    for item in item_details:
       print(item)