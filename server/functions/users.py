from bson import ObjectId
from pymongo.mongo_client import MongoClient
import sys
import os

# Ajout du dossier "server" au chemin de recherche
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from rooms import verify_exist_room_code

client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']

# Création des collections
rooms_collection = db['rooms']
tasks_collection = db['tasks']
rounds_collection = db['rounds']
users_collection = db['users']
messages_collection = db['messages']

def create_user(username,avatar,room_code):
    """
    Cette fonction permet de créer un utilisateur lorsqu'il souhaite rejoindre une room
    
    :param username: nom d'utilisateur
    :param avatar: lien vers l'image de l'avatar choisi
    :param room_code: code de la room à rejoindre
    """

    # Vérification de l'existance de la room que l'utilisateur souhaite rejoindre
    if verify_exist_room_code(room_code):
        user_document = {
            "_id": str(ObjectId()),
            "username": username,
            "avatar": avatar,
            "room_code": room_code   
        }
        # Insertion en base de données
        try:
            users_collection.insert_one(user_document)
        except Exception as e:
            print(f"Erreur lors de l'insertion du document: {e}")
    else : 
        print("La room que vous tentez de rejoindre n'existe pas.")
    return user_document["_id"]