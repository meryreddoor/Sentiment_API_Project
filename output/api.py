from mongoConnection import user_mydb,user_mycol
from mongoConnection import group_mydb,group_mycol

from flask import Flask, request
import json
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

#crea un username y la inserta en la api
#mira que no esté ya asignado.
@app.route('/user/create/<name>',methods=["GET"])
def new_users(name):
    names = (user_mycol.distinct("name"))
    if name in names:
        return "Name already exists"
    else:
        if names:
            n = max(user_mycol.distinct("_id"))+1
        else:
            n = 1
        mydict = {"name":name,"_id":n}
        x = user_mycol.insert_one(mydict)
        return "User inserted"

@app.route('/chat/create/<chat>',methods=["GET"])
def new_chat(chat):
    chats=(group_mycol.distinct("chat"))
    if chat in chats:
        return "Chat already exists"
    else:
        if chats:
            n = max(group_mycol.distinct("_id"))+1
        else:
            n = 1
        mydict = {"chat":chat,"_id":n,"user_name":[],"mensajes":[]}
        x = group_mycol.insert_one(mydict)
        return "Chat inserted"

@app.route('/chat/<_id>/adduser/<user_name>',methods=["GET"])
def new_user_chat(user_name,_id):
    names=(group_mycol.distinct("user_name"))
    if user_name in names:
        return "Name already exists"
    else:
        if names:
            n = max(group_mycol.distinct("_id"))+1
        else:
            n = 1
        usuarios=group_mycol.update({"_id":int(_id)},{"$push":{"user_name":user_name}})
        return "User inserted"

@app.route('/chat/<_id>/mensajes/<mensajes>/adduser/<user_name>',methods=["GET"])
def new_mensajes_chat(mensajes,_id,user_name):
    names=(group_mycol.distinct("user_name"))
    if user_name in names:
        mensajes=group_mycol.update({"_id":int(_id)},{"$push":{"mensajes":{"autor":user_name,"texto":mensajes}}})
        return "This user is in the group, corresponding text inserted"
    else:
        return "This user is not in the group, try with different"

@app.route('/chat/<chat_id>/list',methods=["GET"])
def getList(chat_id):
    chats=(group_mycol.distinct("_id"))
    if int(chat_id) in chats:
        mensajes=group_mycol.find({"_id":int(chat_id)},{"_id":0,"mensajes":1})
        return dumps(mensajes)
    else:
        return "This _id is not in MongoDB"

app.run("0.0.0.0", 5000, debug=True)