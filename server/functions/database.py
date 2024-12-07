import pandas as pd
from bson import ObjectId
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from rooms import verify_exist_room_code, generate_room_code
from backlog import backlog_json_to_df

client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']

# Création des collections
rooms_collection = db['rooms']
tasks_collection = db['tasks']
rounds_collection = db['rounds']
users_collection = db['users']
messages_collection = db['messages']

#create_user("Amine", "link.jpg", "KBQ-IH6")
#users_in_room = get_users_in_room("KBQ-IH6")
#print(len(users_in_room["users"]))
#print(get_votes_for_task_in_round("6743523d26a0c57daf7beef9"))
#create_round("")
#create_room("Projet Test", "strict", "server/tests/files/backlog_valid.json", "Elias", "userpp.jpg")
export_backlog_to_json("FTR-LYE")