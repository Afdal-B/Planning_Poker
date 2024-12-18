"""
Ce module regroupe l'ensemble des fonctions permettant d'intéragir avec les salons de jeu "rooms".
"""
import sys
sys.path.append('/server/functions')
import string, random
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from .backlog import backlog_json_to_df, upload_backlog

client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']

rooms_collection = db['rooms']
tasks_collection = db['tasks']
rounds_collection = db['rounds']
users_collection = db['users']
messages_collection = db['messages']

def create_room(room_name, game_rule, backlog_json, username_creator, avatar_creator) -> dict:
    """
    Cette fonction permet de créer une room en base de données.

    :param room_name: Le nom de la room.
    :param game_rule: La règle de jeu choisie pour cette partie.
    :param backlog_json: Le fichier du backlog au format json.
    :param username_creator: Le nom d'utilisateur du créateur de la room.
    :param avatar_creator: L'avatar du créateur de la room.
    :return: Un dictionnaire contenant le room_code et le user_id du créateur, ou un message d'erreur.
    """
    # import à ce niveau pour éviter une boucle entre les boucles entre les modules
    from .users import create_user

    try:
        # Vérification et chargement du backlog json dans une DataFrame
        backlog = backlog_json_to_df(backlog_json)

        if backlog.empty:
            return {"error": "Le backlog est vide ou invalide."}

        # Génération du room_code
        room_code = generate_room_code()

        # Chargement des tâches en base de données et récupération des ids
        tasks_ids = upload_backlog(backlog, room_code)

        # Création du document de la room
        room_document = {
            "_id": str(ObjectId()),
            "room_name": room_name,
            "room_code": room_code,
            "creator_user_id": None,
            "backlog": tasks_ids,
            "chat": [],
            "current_round": None,
            "game_rule": game_rule,
        }

        # Insertion de la room dans la base de données
        rooms_collection.insert_one(room_document)

        # Création de l'utilisateur (le créateur de la room)
        creator_user_id = create_user(username_creator, avatar_creator, room_code)

        # Mise à jour du document de la room avec l'ID du créateur
        rooms_collection.update_one(
            {"room_code": room_code},
            {"$set": {"creator_user_id": creator_user_id}}
        )

        # Renvoie du dictionnaire avec le room code et l'user id du créateur
        return {"room_code": room_code, "creator_user_id": creator_user_id}

    except Exception as e:
        print(f"Erreur lors de l'insertion de la room ou de l'utilisateur: {e}")
        return {"error": f"Une erreur est survenue: {str(e)}"}

    
def get_users_in_room(room_code: str) -> dict:
    """
    Récupère tous les utilisateurs ayant rejoint une salle spécifique via un code room.
    
    :param room_code: Le code unique de la room.
    :return: La liste des utilisateurs ou un message d'erreur.
    """
    
    # Recherche de la room correspondante
    room = rooms_collection.find_one({"room_code": room_code})
    if not room:
        return {"error": "Room non trouvée"}
    
    # Recherche des utilisateurs ayant rejoint cette salle
    users = users_collection.find({"room_code": room["room_code"]}, {"username": 1, "avatar": 1})
    
    # Conversion des résultats en liste
    user_list = list(users)
    
    if not user_list:
        return {"error": "Aucun utilisateur trouvé dans cette salle"}
    
    # Formatage de la réponse
    return user_list

def verify_exist_room_code(room_code)->bool:
    """
    Cette fonction vérifie l'unicité des code rooms qui sont générés aléatoirement.
    La fonction retourne True si le room_code existe en base de données, False sinon.

    :param room_code: Code la room à vérifier
    """
    existing_room = db.rooms.find_one({'room_code': room_code})
    if existing_room:
        return True
    else:
        return False  
    

def generate_room_code()->str:
    """
    Cette fonction génère un code d'accès à une room de 6 caractères. Le code suivra la structure suivante : XXX-XXX
    """
    characters = string.ascii_letters + string.digits
    while True:
        room_code = ''.join(random.choice(characters) for _ in range(6))
        room_code = room_code[:3] + '-' + room_code[3:]
        room_code = str.upper(room_code)
        if not verify_exist_room_code(room_code):
            return room_code
        
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