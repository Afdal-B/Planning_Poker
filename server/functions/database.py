import pandas as pd
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']

# Création des collections
rooms_collection = db['rooms']
tasks_collection = db['tasks']
rounds_collection = db['rounds']
users_collection = db['users']
messages_collection = db['messages']


def upload_backlog(backlog_df, room_code)->list: 
    """
    Cette fonction permet d'uploader un backlog importé au format JSON et et insère chaque tâche dans la base de données MongoDB.
    Le backlog doit contenir 3 champs par tâche : "En tant que", "Fonctionnalité" et "Objectif".

    :param backlog: DataFrame contenant le backlog à uploader.
    :type backlog_json: pd.DataFrame
    :param room_code: Code la room dans laquelle le backlog est chargé

    :return task_ids: renvoie la liste des id des tâches chargées depuis le backlog
    """

    # Liste des tâches du backlog
    task_ids = []

    if not backlog_df.empty :
        # Récupération et insertion de chaque tâche en base de données
        for _,task in backlog_df.iterrows():
            task_document = {
                "_id": str(ObjectId()),
                "room_id": room_code,
                "en_tant_que": task.get("en_tant_que"),
                "fonctionnalite": task.get("fonctionnalite"),
                "objectif": task.get("objectif"),
                "estimation": None,
                "rounds": []
            }

            try:
                tasks_collection.insert_one(task_document)
                task_ids.append(task_document["_id"])
            except Exception as e:
                print(f"Erreur lors de l'insertion du document: {e}")
        return task_ids
    return []