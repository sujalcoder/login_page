from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://root:root@tech1.kglkjga.mongodb.net/?appName=Tech1")
db = client["login_db"]
users = db["users"]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/check', methods=['POST'])
def check():
    username = request.form['username']
    password = request.form['password']

    user = users.find_one({
        "username": username,
        "password": password
    })

    if user:
        return render_template('success.html', username=username)
    else:
        return "Invalid Username or Password"

if __name__ == '__main__':
    app.run(debug=True)