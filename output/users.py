import pymongo
from flask import Flask, request

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["emotions"]
mycol = mydb["users"]

@app.route('/users/create/<name>')
def new_users(name):
    mydict = {"name":name}
    x = mycol.insert_one(mydict)
    return x

app.run("0.0.0.0", 5000, debug=True)