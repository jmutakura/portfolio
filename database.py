# import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://jmutakura:Jonathan101@cluster0-yedya.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["portfolio"]
collection = db["contacts"]


def insert_to_mongo(data):
    collection.insert_one(data)
