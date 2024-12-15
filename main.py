import os 
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from server.functions.rooms import create_room
from server.functions.users import create_user
from server.functions.backlog import export_backlog_to_json
from server.functions.rounds import vote_for_task_in_round
from flask_socketio import SocketIO, emit, join_room
from server.functions.chat import send_message, add_reaction, fetch_chat_history

# Initialisation de l'application Flask 
app = Flask(__name__)
#Récupération de la clé secrète
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
#Initialisation de l'objet SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

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

    return jsonify({"user_id":user_id})

@app.route('/<round_id>/vote', methods = ['GET', 'POST'])
def vote_round_route(round_id):
    """
    Cette route permet à un utilisateur de voter dans un round.
    """
    # Récupération des données envoyées depuis le front-end
    data = request.get_json()

    # Récupération des autres informations
    user_id = data.get('user_id')
    vote_value = data.get('vote_value')

    # Appel de la fonction pour l'envoi en base de données
    vote_for_task_in_round(round_id, user_id, vote_value)

    return 'Hello, World!'

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