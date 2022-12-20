import os
from pymongo import MongoClient

client = MongoClient(os.environ["MONGODB_URI"])
db = client.get_database("busse")

sales_tracings_local = db.get_collection("sales")
