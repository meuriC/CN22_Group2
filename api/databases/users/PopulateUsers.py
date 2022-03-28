from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import sys
import csv

csv.field_size_limit(sys.maxsize)

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "CN_Grupo11"
password = "jcAUsQouhCddO0xW"
credentials = user + ":" + password

client = MongoClient("mongodb+srv://"+credentials+"@users.lastb.mongodb.net/test")
db = client["database"]

# drop col
db.drop_collection("users")

db = db["users"]


# author.steamid,   17
# author.num_games_owned,    18
# author.num_reviews,   19
# author.playtime_forever,    20
# author.playtime_at_review,   22
# author.last_played,   23


insert_list = []
count = 0
total = 2_000_000

with open("api/databases/users/users.csv","r",encoding="ISO-8859-1") as f:

    reader = csv.reader(f)
    first_elem = True
    print('Populating the DB ...')

    for row in reader:
        
        if count >= 2_000_000: #stop populating
            break

        if first_elem:
            first_elem = False
            continue

        count+=1

        users = {
                'steamid' : row[2],
                'num_games_owned': row[3],
                'num_reviews' : row[4],
                'playtime_forever' : row[5],
                'playtime_at_review' : row[6],
                'last_played' : row[7]
        }
    
        insert_list.append(users)

        # insert
        if len(insert_list) >= 100_000:
            result = db.insert_many(insert_list)
            insert_list = []

            
# insert rest
if insert_list != []:
    result = db.insert_many(insert_list)
    insert_list = []

print('\nSuccess')