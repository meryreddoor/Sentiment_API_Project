from mongoConnection import user_mydb,user_mycol
from mongoConnection import group_mydb,group_mycol
from flask import Flask, request

app = Flask(__name__)

#crea un username y la inserta en la api
#mira que no esté ya asignado.
@app.route('/users/create/<name>')
def new_users(name):
    names = (user_mycol.distinct("name"))
    if name in names:
        return "Name already exists"
    else:
        if names:
            n = max(user_mycol.distinct("user_id"))+1
        else:
            n = 1
        mydict = {"name":name,"user_id":n}
        x = user_mycol.insert_one(mydict)
        return "User inserted"

@app.route('/chat/create/<chat>')
def new_chat(chat):
    chats=(group_mycol.distinct("chat"))
    if chat in chats:
        return "Chat already exists"
    else:
        if chats:
            n = max(group_mycol.distinct("chat_id"))+1
        else:
            n = 1
        mydict = {"chat":chat,"chat_id":n,"user_name":[],"mensajes":[]}
        x = group_mycol.insert_one(mydict)
        return "Chat inserted"

@app.route('/chat/<chat_id>/adduser/<user_name>',methods=["GET"])
def new_user_chat(user_name,chat_id):
    usuarios=group_mycol.update({"chat_id":int(chat_id)},{"$push":{"user_name":user_name}})
    return "User inserted"
app.run("0.0.0.0", 5000, debug=True)
















"""
@app.route('/users/create/chat/<chat>/<name>')
def getName(chat,name):
    emotions = client.get_default_database()["users"]
    namereg = re.compile(name, re.IGNORECASE)
    query = emotions.find_one({"name": namereg})
    if not query:
        raise ValueError("Name not found")
    return dumps(query)

def new_chat(chat,user_id,name):
    chats =(group_mycol.distinct("chat"))
    names=(group_mycol.distinct("name"))
    user_ids=(group_mycol.distinct("user_id"))
    if chat in chats:
        return "Chat name already exists"
    elif user_id in user_ids:
        return "User id already exists"
    else:
        if names:
            n = max(group_mycol.distinct("user_id"))+1
        else:
            n = 1
        mydict = {"chat":chat,"name":getName(name),"user_id":n}
        x = group_mycol.insert_one(mydict)
        return "Chat inserted"
"""