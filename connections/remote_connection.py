import os
from pymongo import MongoClient

client = MongoClient(os.environ["ATLAS_MONGODB_URI"])
db = client.get_database("busserebatetraces")

rebate_tracings_collection = db.get_collection("tracings")
sales_tracings_collection = db.get_collection("sales_tracings")

sched_data = db.get_collection("sched_data")
