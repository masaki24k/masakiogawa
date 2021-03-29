import requests
import json
from user import User

r = requests.get("https://api.sheety.co/f08e3b1b55ba18dc000f0d6abbe26a78/test/userdata")
s = r.json()["userdata"]  # シート名

users = []
for i in range(len(s)):
    useri = User(s[i]["id"],
                 s[i]["username"],
                 s[i]["email"],
                 s[i]["password"])
    users.append(useri)

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
