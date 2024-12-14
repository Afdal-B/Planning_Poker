import os 
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room
from server.functions.chat import send_message, add_reaction, fetch_chat_history

# Initialisation de l'application Flask et de SocketIO
app = Flask(__name__)
#Récupération de la clé secrète
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
#Initialisation de l'objet SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def create_user():
    """
    Cette route permet de 
    """
    #room_data = request.get_json()
    #room_name = room_data.get('room_name')
    #username_creator = room_data.get('username_creator')
    #avatar_creator = room_data.get('avatar_creator')
    #game_rule = room_data.get('game_rule')

    #create_room(room_name,game_rule,backlog_json,username_creator, avatar_creator)

    return 'Hello, World!'

