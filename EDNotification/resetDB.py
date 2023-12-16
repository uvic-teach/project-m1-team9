import json

data = [{"name": "John", "email": "mistered.health@gmail.com", "nearestED": "Victoria General Hopsital", "EDqueue": 5}, 
{"name": "Emily", "email": "mistered.health@gmail.com", "nearestED": "Royal Jubilee Hospital", "EDqueue": 2}, 
{"name": "Sam", "email": "mistered.health@gmail.com", "nearestED": "Oak Bay Urgent Care Clinic", "EDqueue": 0}]


file_path = "mockDB.json"
with open(file_path, 'w') as openfile:
    json.dump(data, openfile)
