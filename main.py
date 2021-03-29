from flask import Flask, request, render_template
import json
import requests
from user import User
import cgi
import sys
import io

app = Flask(__name__)

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

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method=="GET":
        return render_template("login.html")
    else:
        form_username = request.form['username']
        form_password = request.form['password']
        form_user = username_table.get(form_username, None)
        if form_user and form_user.password == form_password:
            return "Success"

if __name__ == '__main__':
    app.run(debug=True)


#r = requests.get("https://api.sheety.co/f08e3b1b55ba18dc000f0d6abbe26a78/test/userdata")
#s = r.json()["userdata"]  # シート名

#users = []
#for i in range(len(s)):
#    useri = User(s[i]["id"],
#                 s[i]["username"],
#                 s[i]["email"],
#                 s[i]["password"])
#    users.append(useri)

#username_table = {u.username: u for u in users}
#userid_table = {u.id: u for u in users}


#@app.route('/login', methods=['GET'])
#def login(username, password):
#    user = username_table.get(username, None)
#    if user and user.password == password:
#        return user