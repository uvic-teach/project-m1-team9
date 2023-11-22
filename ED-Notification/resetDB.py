import json

data = [{"name": "John", "email": "<INSERT YOUR EMAIL>", "nearestED": "Victoria General Hopsital", "EDqueue": 5}, 
{"name": "Emily", "email": "<INSERT YOUR EMAIL>", "nearestED": "Royal Jubilee Hospital", "EDqueue": 2}, 
{"name": "Sam", "email": "<INSERT YOUR EMAIL>", "nearestED": "Oak Bay Urgent Care Clinic", "EDqueue": 0}]


file_path = "mockDB.json"
with open(file_path, 'w') as openfile:
    json.dump(data, openfile)
