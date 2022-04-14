from pymongo import MongoClient

from pprint import pprint
import collections
import sys
import csv

csv.field_size_limit(sys.maxsize)


client = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@games.2gyca.mongodb.net/test")
db = client["database"]

# drop everything in there
db.drop_collection("games")

db = db["games"]


# app_id,      0
# app_name,    1
# number_reviews,  2 


insert_list = []

with open("api/databases/games/games.csv","r") as f:

    reader = csv.reader(f)
    first_elem = True
    print('Populating the DB ...')

    for row in reader:
        
        if first_elem:
            first_elem = False
            continue
        
        games = {
                'id' : row[0],
                'name': row[1].strip(),
                'reviews_number' : row[2]
        }
    
        insert_list.append(games)

        # insert
        if len(insert_list) >= 100_000:
            result = db.insert_many(insert_list)
            insert_list = []

# insert rest
if len(insert_list) > 0:
    result = db.insert_many(insert_list)
    insert_list = []

print('\nSuccess')