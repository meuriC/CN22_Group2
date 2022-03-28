from unittest import skip
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

client = MongoClient("mongodb+srv://"+credentials+"@reviews2.qwqeh.mongodb.net/test")
db = client["database"]

# drop everything in there
db.drop_collection("reviews")

db = db["reviews"]


# app_id,   1
# review_id,    2
# review,   4
# recommended,    7
# timestamp_created,   5
# timestamp_updated,   6
# votes_helpful,    8
# author.steamid,   9
# language,   3


insert_list = []
count = 0
total = 2_000_000

with open("api/databases/reviews/steam_reviews_3.csv","r",encoding="ISO-8859-1") as f:

    reader = csv.reader(f)
    first_elem = True
    print('Populating the DB ...')

    for row in reader:
        
        if count >= total:  #stop populating
            break

        if first_elem:
            first_elem = False
            continue
        
        count+=1

        if count < 1_000_000:  #dont want to populate with the same docs
            continue

        reviews = {
                'app_id' : row[2],
                'review_id': row[4],
                'language' : row[5],
                'review' : row[6].strip(),
                'timestamp_created' : row[7],
                'timestamp_updated' : row[8],
                'recommended' : row[9],
                'votes_helpful' : row[10],
                'author.steamid' : row[17]
        }

        # append
        if count >= 1_000_000:  #start populating
           
            insert_list.append(reviews)
   
        # insert
        if len(insert_list) >= 50_000:
            result = db.insert_many(insert_list)
            insert_list = []
            
# insert rest
if insert_list != []:
    result = db.insert_many(insert_list)
    insert_list = []


print('\nSuccess')