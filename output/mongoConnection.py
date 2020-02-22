import pymongo

#Conexión con la colección usuarios
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
user_mydb = myclient["emotions"]
user_mycol = user_mydb["users"]

#Conexión con la colección conversations
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
conv_mydb = myclient["emotions"]
conv_mycol = conv_mydb["conversations"]

#Conexión con la colección grupos
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
group_mydb = myclient["emotions"]
group_mycol = group_mydb["groups"]