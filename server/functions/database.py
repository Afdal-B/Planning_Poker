import pandas as pd
from bson import ObjectId
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


    
def create_room(room_name,game_rule,backlog_json,creator_user_id)->str:
    """
    Cette fonction permet de créer une room en base de données
    
    """
    
    # Vérification et chargement du backlog json dans une DataFrame
    backlog = backlog_json_to_df(backlog_json)

    if not backlog.empty:
        # Génération du room_code
        room_code = generate_room_code()

        # Chargement des tâches en base de données et récupération des ids
        tasks_ids = upload_backlog(backlog, room_code)

        room_document = {
            "_id": str(ObjectId()),
            "room_name" : room_name,
            "room_code": room_code, 
            "creator_user_id": creator_user_id,
            "backlog": tasks_ids,
            "chat": [],
            "current_round": None, 
            "game_rule": game_rule,
        }

        # Insertion en base de données
        try:
            rooms_collection.insert_one(room_document)
        except Exception as e:
            print(f"Erreur lors de l'insertion du document: {e}")
            
        return room_code
    

def create_round(task_id, room_id, timer):
    """
    Cette fonction permet de créer un round en base de données pour une tâche d'une room, et de lui attribué un temps imparti.
    
    :param task_id: id de la tâche à laquelle les utilisateurs doivent voter.
    :param room_id: id de la room dans laquelle les utilisateurs doivent voter.
    :param timer: temps imparti pour ce round.
    
    """
    round_document = {
        "_id": str(ObjectId()),
        "task_id": task_id,
        "room_id": room_id,
        "timer": timer,
        "votes": [],
        "is_active": True,
        "results_visible": False
    }

    try:
        rounds_collection.insert_one(round_document)
    except Exception as e:
        print(f"Erreur lors de l'insertion du document: {e}")
        return None
    return round_document["_id"]

def vote_for_task_in_round(round_id: str, user_id: str, vote_value: str) -> dict:
    """
    Cette fonction permet à un utilisateur de voter pour une tâche dans un round spécifique.
    
    :param round_id: L'ID du round dans lequel l'utilisateur vote.
    :param user_id: L'ID de l'utilisateur qui vote.
    :param vote_value: La valeur du vote
    :return message dict: Un message de succès ou une erreur.
    """
    
    # Recherche du round dans la base de données
    round = rounds_collection.find_one({"_id": round_id})
    if not round:
        return {"error": "Round non trouvé"}
    
    # Vérification si le round est actif
    if not round['is_active']:
        return {"error": "Le round n'est plus actif, impossible de voter"}
    
    # Vérification si l'utilisateur a déjà voté
    existing_vote = next((vote for vote in round['votes'] if vote['user_id'] == user_id), None)
    if existing_vote:
        return {"error": "L'utilisateur a déjà voté"}
    
    # Ajout du vote à la liste des votes dans le round
    new_vote = {
        "user_id": user_id,
        "vote": vote_value,
        "voted_at": datetime.now()  # Ajout de la date et heure du vote
    }
    
    # Mise à jour de la collection "rounds" avec le nouveau vote
    try:
        rounds_collection.update_one(
            {"_id": round_id},
            {"$push": {"votes": new_vote}}
        )
    except Exception as e:
        return {"error": f"Erreur lors de l'ajout du vote: {e}"}
    
    return {"message": "Vote ajouté avec succès"}
