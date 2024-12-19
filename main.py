import os 
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from time import time, sleep
from threading import Thread
from server.functions.rooms import create_room, get_users_in_room
from server.functions.users import create_user
from server.functions.backlog import export_backlog_to_json, get_all_tasks, next_task
from server.functions.rounds import vote_for_task_in_round, create_round
from flask_socketio import SocketIO, emit, join_room
from server.functions.chat import send_message, add_reaction, fetch_chat_history
from threading import Timer
import threading

# Initialisation de l'application Flask 
app = Flask(__name__)
#Récupération de la clé secrète
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
#Initialisation de l'objet SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")
timers = {}
CORS(app)

@app.route('/create_room', methods = ['GET', 'POST'])
def create_room_route():
    """
    Cette route permet de créer une room depuis les données du front-end à l'aide de la fonction "create_room"
    """
    # Récupération des données envoyées depuis le front-end
    data = request.get_json()

    # Récupération et nettoyage du backlog
    backlog = data['backlog_json']
    backlog = backlog.replace("\n","")

    # Récupération des autres informations du formulaire
    room_name = data.get('room_name')
    username_creator = data.get('username_creator')
    avatar_creator = data.get('avatar_creator')
    game_rule = data.get('game_rule')

    # Appel de la fonction pour l'envoi en base de données
    data_dict = create_room(room_name,game_rule,backlog,username_creator, avatar_creator)

    # Renvoie du room code et de l'user_id du createur au front-end
    return jsonify(data_dict)

@app.route('/join_room', methods = ['GET', 'POST'])
def join_room_route():
    """
    Cette route permet de rejoindre une room depuis les données du front-end à l'aide de la fonction "create_user"
    """
    # Récupération des données envoyées depuis le front-end
    data = request.get_json()

    # Récupération des autres informations du formulaire
    username = data.get('username')
    avatar = data.get('avatar')
    room_code = data.get('room_code')

    # Appel de la fonction pour l'envoi en base de données
    user_id = create_user(username, avatar, room_code)

    return jsonify({"user_id":user_id, "room_code":room_code})

@app.route('/vote', methods = ['GET', 'POST'])
def vote_round_route():
    """
    Cette route permet à un utilisateur de voter dans un round.
    """
    # Récupération des données envoyées depuis le front-end
    data = request.get_json()

    # Récupération des autres informations
    round_id = data.get('round_id')
    user_id = data.get('user_id')
    vote_value = data.get('vote_value')

    # Appel de la fonction pour l'envoi en base de données
    vote_for_task_in_round(round_id, user_id, vote_value)

    return

@app.route('/users', methods = ['GET', 'POST'])
def users_route():
    """
    Cette route permet d'afficher touts les utilisateurs de la room'
    """
    # Récupération des données envoyées depuis le front-end
    data = request.get_json()

    # Récupération des autres informations du formulaire
    room_code = data.get('room_code')

    # Appel de la fonction pour l'envoi en base de données
    users = get_users_in_room(room_code)

    return jsonify({"users": users})

@app.route('/backlog', methods = ['GET', 'POST'])
def backlog_route():
    """
    Cette route permet d'afficher toutes les tâches du backlog'
    """
    # Récupération des données envoyées depuis le front-end
    data = request.get_json()

    # Récupération des autres informations du formulaire
    room_code = data.get('room_code')

    # Appel de la fonction pour l'envoi en base de données
    tasks = get_all_tasks(room_code)

    return jsonify({"tasks": tasks})

@app.route('/export_backlog', methods = ['GET', 'POST'])
def export_backlog_route():
    """
    Cette route permet de récupérer le room code et l'afficher sur le front-end pour que le créateur de la room puisse le partager
    """
    # Récupération des données envoyées depuis le front-end
    #data = request.get_json()

    # Récupération des autres informations du formulaire
    #room_code = data.get('room_code')

    # Appel de la fonction pour l'envoi en base de données
    #export_backlog_to_json(room_code)

    return 'Hello, World!'

@socketio.on('members')
def get_members(data):
    """
    Cette route permet d'afficher touts les utilisateurs de la room'
    """
    # Récupération des données envoyées depuis le front-end

    # Récupération des autres informations du formulaire
    room_code = data.get('room_code')
    # Appel de la fonction pour l'envoi en base de données
    users = get_users_in_room(room_code)

    emit("get_members",{"members":users},to=room_code)
    join_room(room_code)

@socketio.on('create_round')
def create_round_socket(data):
    """
    Gestion de l'événement Socket.IO pour créer un round
    """
    # Récupération des données envoyées par le frontend
    room_code = data.get('room_code')

    # Appel des fonctions pour obtenir la tâche et créer le round
    task = next_task(room_code)
    if not task:
        emit('error', {"message": "No task available for this room"}, to=request.sid)
        return

    round_id = create_round(task["_id"], room_code)

    # Envoyer les données à tous les utilisateurs de la room
    emit('round_created', {"round_id": round_id, "task": task}, to=room_code)

    # Joindre la room pour synchronisation
    join_room(room_code)


@app.route('/round', methods = ['GET', 'POST'])
def display_round_route():
    """
    Cette route de créer un round
    """
    # Récupération des données envoyées depuis le front-end
    data = request.get_json()

    # Récupération des autres informations du formulaire
    room_code = data.get('room_code')

    # Appel de la fonction pour l'envoi en base de données
    task = next_task(room_code)
    print(task)

    round_id = create_round(task["_id"], room_code)

    return jsonify({"round_id":round_id, "task":task})
 
@socketio.on('join_room')
def join_room_event(data):
    room_code = data['room_code']
    join_room(room_code)
    emit('joined_room', {"message": f"User joined room {room_code}"}, to=room_code)


# Route HTTP pour récupérer l'historique des messages d'une room
@app.route('/chat/history/<room_id>', methods=['GET'])
def get_chat_history(room_id):
    """
    Route pour récupérer l'historique des messages d'une room.
    """
    response, status = fetch_chat_history(room_id)
    return jsonify(response), status

# Événement WebSocket pour rejoindre une room et intégrer le chat
@socketio.on('join')
def handle_join(data):
    """
    Un utilisateur rejoint une room et est automatiquement ajouté au chat.
    """
    room_id = data.get('room_id')
    user_id = data.get('user_id')

    if not room_id or not user_id:
        return {"error": "room_id and user_id are required"}, 400

    join_room(room_id)
    print(f"User {user_id} joined room: {room_id}")

# Événement WebSocket pour envoyer un message
@socketio.on('send_message')
def handle_send_message(data):
    """
    Gestion de l'envoi d'un message dans une room.
    """
    response, status = send_message(data)
    if status == 200:
        emit("new_message", data, room=data.get("room_id"))
    return response, status

# Événement WebSocket pour ajouter une réaction
@socketio.on('add_reaction')
def handle_add_reaction(data):
    """
    Gestion de l'ajout de réactions aux messages.
    """
    response, status = add_reaction(data)
    if status == 200:
        emit("reaction_added", data, room=data.get("room_id"))
    return response, status

# Lancer l'application
if __name__ == '__main__':
    socketio.run(app, debug=True)