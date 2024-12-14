from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from server.functions.rooms import create_room
from server.functions.users import create_user
from server.functions.backlog import export_backlog_to_json
app = Flask(__name__)


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
    room_code = create_room(room_name,game_rule,backlog,username_creator, avatar_creator)

    # Renvoie du room code au front-end
    return jsonify({"room_code": room_code})

@app.route('/join_room', methods = ['GET', 'POST'])
def join_room_route():
    """
    Cette route permet de rejoindre une room depuis les données du front-end à l'aide de la fonction "create_user"
    """
    # Récupération des données envoyées depuis le front-end
    #data = request.get_json()

    # Récupération des autres informations du formulaire
    #username = data.get('username')
    #avatar = data.get('avatar')
    #room_code = data.get('room_code')

    # Appel de la fonction pour l'envoi en base de données
    #create_user(username, avatar, room_code)

    return 'Hello, World!'

@app.route('/share_room', methods = ['GET', 'POST'])
def share_room_route():
    """
    Cette route permet de récupérer le room code et l'afficher sur le front-end pour que le créateur de la room puisse le partager
    """
    # Récupération des données envoyées depuis le front-end
    #data = request.get_json()

    # Récupération des autres informations du formulaire
    #username = data.get('username')
    #avatar = data.get('avatar')
    #room_code = data.get('room_code')

    # Appel de la fonction pour l'envoi en base de données
    #create_user(username, avatar, room_code)

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

if __name__ == '__main__':
    app.run(debug=True)