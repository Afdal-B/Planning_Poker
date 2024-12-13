import sys
sys.path.append('/server/functions')
from flask import Flask, request
from flask_cors import CORS
import json
from server.functions.rooms import create_room
app = Flask(__name__)


CORS(app)

@app.route('/create_room', methods = ['GET', 'POST'])
def create_room_route():
    """
    Cette route permet de 
    """
    data = request.get_json()
    backlog = data['backlog_json']
    backlog = backlog.replace("\n","")
    backlog_json = json.loads(backlog)
    print(backlog_json)
    room_name = data.get('room_name')
    username_creator = data.get('username_creator')
    avatar_creator = data.get('avatar_creator')
    game_rule = data.get('game_rule')

    create_room(room_name,game_rule,backlog_json,username_creator, avatar_creator)

    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)