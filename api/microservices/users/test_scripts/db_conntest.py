from bson.objectid import ObjectId  
from pymongo import MongoClient
import pymongo

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@users.lastb.mongodb.net/test"

    # Create a connection using MongoClient. 
    client = MongoClient(CONNECTION_STRING)

    return client['database']
    

if __name__ == "__main__": 
    # Get the database
    dbname = get_database()
	
    collection_name = dbname['users']
    #item_details = collection_name.find({"user_name": "usn76561198054155096"})
    #item_details = list(collection_name.find().limit(5))
    #item_details = collection_name.find({"_id": ObjectId("62439da17e360515056f336b")})
    """item_details = collection_name.insert({ "user_name": "miguelfsilva",
                                            "user_id": 0, 
                                            "user_num_games_owned": 0, 
                                            "user_num_reviews": 0, 
                                            "user_playtime_forever": 0,
                                            "user_playtime_last_two_weeks": 0,
                                            "user_playtime_at_review": 0,
                                            "author_last_played": 0,
                                            "user_pwd": "clear"})"""
	
    for item in item_details:
       print(item)