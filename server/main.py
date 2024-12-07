from flask import Flask, request
app = Flask(__name__)

@app.route('/create_room', methods=["POST"])
def create_user():
    """
    Cette route permet de 
    """
    room_data = request.get_json()
    room_name = room_data.get('room_name')
    username_creator = room_data.get('username_creator')
    avatar_creator = room_data.get('avatar_creator')
    game_rule = room_data.get('game_rule')

    #create_room(room_name,game_rule,backlog_json,username_creator, avatar_creator)

    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)