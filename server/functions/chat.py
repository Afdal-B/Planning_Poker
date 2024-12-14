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

#Définition de la fonction de l'ajout de réaction
def add_reaction(data):
    """
    Cette fonction permet d'ajouter une réaction à un message spécifique.

    :param data: Un dictionnaire contenant les informations de la réaction.
    :return: Un message de confirmation ou d'erreur.
    """
    message_id = data.get("message_id")
    emoji = data.get("emoji")

    if not message_id or not emoji:
        return {"error": "message_id and emoji are required"}, 400

    # Vérification de l'existence du message
    message = messages_collection.find_one({"_id": message_id})
    if not message:
        return {"error": "Message not found"}, 404

    # Initialisation du champ `reactions` si nécessaire
    if f"reactions.{emoji}" not in message:
        messages_collection.update_one(
            {"_id": message_id},
            {"$set": {f"reactions.{emoji}": 0}}
        )

    # Incrémentation du compteur de la réaction
    result = messages_collection.update_one(
        {"_id": message_id},
        {"$inc": {f"reactions.{emoji}": 1}}
    )

    if result.modified_count == 0:
        return {"error": "Failed to update reactions"}, 500

    # Envoi de la réaction aux utilisateurs de la room
    emit("reaction_updated", {
        "message_id": message_id,
        "emoji": emoji,
        "count": message["reactions"].get(emoji, 0) + 1
    }, broadcast=True)

    return {"message": "Reaction added successfully"}, 200
#Définition de la fonction de la récupération des messages
def fetch_chat_history(room_id):
    """
    Cette fonction permet de récupérer l'historique des messages d'une room spécifique.

    :param room_id: L'ID de la room.
    :return: Un dictionnaire contenant la liste des messages et les réactions ou un message d'erreur.
    """
    if not room_id:
        return {"error": "room_id is required"}, 400
    if not ObjectId.is_valid(room_id):
        return {"error": "Invalid ObjectId format."}, 400
    # Recherche de la room correspondante et récupération des IDs des messages
    room = rooms_collection.find_one({"_id": room_id})
    if not room:
        return {"error": "Room not found"}, 404

    message_ids = room.get("chat", [])
    messages = list(messages_collection.find({"_id": {"$in": message_ids}}))


    return {"chat": messages}, 200