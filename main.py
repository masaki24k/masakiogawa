from flask import Flask, request, render_template
import requests
from user import User

app = Flask(__name__)

url = "https://api.sheety.co/f08e3b1b55ba18dc000f0d6abbe26a78/test/userdata"

@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    else:
        form_id = int(request.form['id'])
        form_username = request.form['username']
        form_email = request.form['email']
        form_password = request.form['password']
        adddata = {
                    "userdatum": {
                        "id": form_id,
                        "username": form_username,
                        "email": form_email,
                        "password": form_password
                    }
        }
        requests.post(url, json = adddata)
        return "success"


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

@app.route('/login', methods=["POST", "GET"])
def index():
    if request.method=="GET":
        return render_template("login.html")
    else:
        form_username = request.form['username']
        form_password = request.form['password']
        form_user = username_table.get(form_username, None)
        if form_user and form_user.password == form_password:
            return render_template("afterlogin.html", form_user=form_username)
        elif form_user is None:
            return "please make an account"
        else:
            return "wrong password"

if __name__ == '__main__':
    app.run(debug=True)

