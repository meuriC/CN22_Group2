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

client = MongoClient("mongodb+srv://"+credentials+"@reviews.kqme2.mongodb.net/test")
db = client["database"]

#drop col
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
total = 1_000_000   #docs we want to populate

with open("api/databases/reviews/steam_reviews_3.csv","r") as f:

    reader = csv.reader(f)
    first_elem = True
    print('Populating the DB ...')

    for row in reader:
        
        #stop populating
        if count >= total:
            break

        if first_elem:
            first_elem = False
            continue
        
        count+=1


        reviews = {
                'app_id' : row[2],
                'review_id': row[4],
                'language' : row[5],
                'review' : row[6].strip(),
                'timestamp_created' : row[7],
                'timestamp_updated' : row[8],
                'recommended' : row[9],
                'votes_helpful' : int(row[10]),
                'author_steamid' : row[17]
        }
        
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