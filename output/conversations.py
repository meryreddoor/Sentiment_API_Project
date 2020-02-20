import pymongo
from flask import Flask, request

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["emotions"]
mycol = mydb["conversations"]

@app.route('/users/create/<name>/<conversation>')
def new_conversation(name,conversation):
    mydict = {"name":name,"conversation":conversation}
    x = mycol.insert_one(mydict)
    return x

app.run("0.0.0.0", 5000, debug=True)