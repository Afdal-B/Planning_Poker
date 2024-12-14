# Les fonctionnalités de la messagerie 
# Importation des bibliothèques requises
from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from datetime import datetime
from bson import ObjectId
from flask_socketio import emit, join_room, leave_room

#Connexion à la base de données 
client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']
messages_collection = db['messages']
rooms_collection = db['rooms']

#Définition de la fonction d'envoi de message
def send_message(data):
    """
    Cette fonction permet d'envoyer un message dans une room spécifique et l'enregistre en base de données.

    :param data: Un dictionnaire contenant les informations du message.
    :return: Un message de confirmation ou d'erreur.
    """
    room_id = data.get('room_id')
    user_id = data.get('user_id')
    content = data.get('content')

    if not room_id or not user_id or not content:
        return {"error": "room_id, user_id, and content are required"}, 400
    
    message_id=str(ObjectId())

    # Construction de l'objet message
    message = {
        "_id": message_id,
        "room_id": room_id,
        "user_id": user_id,
        "content": content,
        "sent_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "reactions": {}  # Initialisation des réactions comme un dictionnaire vide
    }

    # Sauvgarde du message en base de données
    messages_collection.insert_one(message)

    # Ajout de l'ID du message à la liste des messages de la room
    rooms_collection.update_one(
        {"_id": room_id},
        {"$push": {"chat": message_id}}
    )

    # Envoi du message aux utilisateurs de la room
    emit("new_message", {
        "_id": message_id,
        "room_id": room_id,
        "user_id": user_id,
        "content": content,
        "sent_at": message["sent_at"],
        "reactions": message["reactions"]
    }, room=room_id)
    return {"message": "Message sent successfully"}, 200

