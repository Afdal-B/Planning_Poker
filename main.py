from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": "http://localhost:3000",
                                 "allow_headers": ["Origin", "Authorization", "X-Frame-Options", "X-Requested-With", "DNT", "User-Agent", "If-Modified-Since", "Cache-Control", "Range", "X-Real-IP", "HOST", "X-NginX-Proxy", "Content-Type", "If-Match"],
                                 "expose_headers": ["ETag", "Content-Length", "Content-Range", "Access-Control-Allow-Origin"],
                                 "max_age": "3600"}})

@app.route('/create_room', methods = ['GET', 'POST'])
def create_room():
    """
    Cette route permet de 
    """
    data = request.get_json()
    print(type(data['backlog_json']))
    print(data)
    #room_data = request.get_json()
    #room_name = room_data.get('room_name')
    #username_creator = room_data.get('username_creator')
    #avatar_creator = room_data.get('avatar_creator')
    #game_rule = room_data.get('game_rule')

    #create_room(room_name,game_rule,backlog_json,username_creator, avatar_creator)

    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)