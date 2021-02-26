import pymongo
import datetime

client = pymongo.MongoClient('mongodb://username:password@IPAddress/')

db = client['Database Name']

users = db['users']

def add_user(username, password, first_name, email, gender, location, age):
    document = {
        'Username' : username,
        'Password' : password,
        'First Name' : first_name,
        'Email' : email,
        'Gender:' : gender,
        'Location' : location,
        'Age Bracket' : age,
        'Join Date' : datetime.datetime.now()
    }
    return users.insert_one(document)

#Retrieval

results = users.find({})
for result in results:
    print(result)
