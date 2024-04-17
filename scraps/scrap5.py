import json

data = {
    "website": {
        "username" : 'sam@yahoo.com',
        "password" : 1234
    }
}

print(json.dumps(data))

print(data)