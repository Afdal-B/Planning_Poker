"""
Ce module regroupe l'ensemble des fonctions permettant d'intéragir les utilisateurs jouant une partie de Planning Pocker.
"""

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

def create_user(username, avatar, room_code):
    """
    Cette fonction permet de créer un utilisateur lorsqu'il souhaite rejoindre une room.
    
    :param username: nom d'utilisateur
    :param avatar: lien vers l'image de l'avatar choisi
    :param room_code: code de la room à rejoindre
    """

    # Vérification de l'existence de la room
    if not verify_exist_room_code(room_code):
        print("La room que vous tentez de rejoindre n'existe pas.")
        return None

    # Vérification si le username est déjà utilisé dans cette room
    existing_user = users_collection.find_one({"room_code": room_code, "username": username})
    if existing_user:
        print(f"Le nom d'utilisateur '{username}' est déjà pris dans cette room. Veuillez en choisir un autre.")
        return None

    # Si le nom d'utilisateur est disponible, création de l'utilisateur
    user_document = {
        "_id": str(ObjectId()),
        "username": username,
        "avatar": avatar,
        "room_code": room_code   
    }

    # Insertion en base de données
    try:
        users_collection.insert_one(user_document)
        print(f"L'utilisateur {username} a été créé avec succès dans la room {room_code}.")
    except Exception as e:
        print(f"Erreur lors de l'insertion du document: {e}")
        return None
    
    return user_document["_id"]
