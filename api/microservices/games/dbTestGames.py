from bson.objectid import ObjectId  
from pymongo import MongoClient
import pymongo

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@games.2gyca.mongodb.net/test"

    # Create a connection using MongoClient. 
    client = MongoClient(CONNECTION_STRING)

    return client['database']
    

if __name__ == "__main__": 
    # Get the database
    dbname = get_database()
    
    collection_name = dbname['games']
    #item_details = collection_name.find({"_id": ObjectId("62431134bad164db48a16edd")}) # IT WORKS
    #item_details = collection_name.find({"id": "203160"})  # IT WORKS
    #item_details = collection_name.find({"id": {"$all": ["219150"]} }).limit(3)  # IT WORKS
    item_details = collection_name.find().skip(44).limit(3)
	
    for item in item_details:
       print(item)