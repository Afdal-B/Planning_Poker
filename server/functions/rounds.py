"""
Ce module regroupe l'ensemble des fonctions permettant d'intéragir avec les rounds d'une partie de Planning Pocker.
"""

from bson import ObjectId
from pymongo.mongo_client import MongoClient
from datetime import datetime
from .rooms import get_users_in_room
from .backlog import next_task, add_estimation_task


client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']

# Création des collections
rooms_collection = db['rooms']
tasks_collection = db['tasks']
rounds_collection = db['rounds']
users_collection = db['users']

def create_round(task_id, room_code):
    """
    Cette fonction permet de créer un round en base de données pour une tâche d'une room, et de lui attribué un temps imparti.
    
    :param task_id: id de la tâche à laquelle les utilisateurs doivent voter.
    :param room_code: code de la room dans laquelle les utilisateurs doivent voter.
    :param timer: temps imparti pour ce round.
    
    """
    round_document = {
        "_id": str(ObjectId()),
        "task_id": task_id,
        "room_code": room_code,
        "votes": []
    }

    try:
        rounds_collection.insert_one(round_document)
    except Exception as e:
        print(f"Erreur lors de l'insertion du document: {e}")
        return None
    return round_document["_id"]

def vote_for_task_in_round(round_id: str, user_id: str, vote_value: str) -> dict:
    """
    Cette fonction permet à un utilisateur de voter pour une tâche dans un round spécifique.
    
    :param round_id: L'ID du round dans lequel l'utilisateur vote.
    :param user_id: L'ID de l'utilisateur qui vote.
    :param vote_value: La valeur du vote
    :return message dict: Un message de succès ou une erreur.
    """
    
    # Recherche du round dans la base de données
    round = rounds_collection.find_one({"_id": round_id})
    if not round:
        return {"error": "Round non trouvé"}
    
    # Ajout du vote à la liste des votes dans le round
    new_vote = {
        "user_id": user_id,
        "vote": vote_value,
        "voted_at": datetime.now()
    }
    
    # Mise à jour de la collection "rounds" avec le nouveau vote
    try:
        rounds_collection.update_one(
            {"_id": round_id},
            {"$push": {"votes": new_vote}}
        )
    except Exception as e:
        return {"error": f"Erreur lors de l'ajout du vote: {e}"}
    
    return {"message": "Vote ajouté avec succès"}

def get_votes_for_task_in_round(round_id: str) -> dict:
    """
    Récupère l'ensemble des votes pour une tâche spécifique dans un round, 
    avec les détails des utilisateurs (nom d'utilisateur et avatar).
    
    :param round_id: L'ID du round pour lequel récupérer les votes.
    :return: Un dictionnaire contenant la liste des votes avec les informations des utilisateurs.
    """
    
    # Recherche du round dans la base de données
    round = rounds_collection.find_one({"_id": round_id})
    if not round:
        return {"error": "Round non trouvé"}
    
    # Vérification si des votes existent
    votes = round.get("votes", [])
    if not votes:
        return {"error": "Aucun vote trouvé pour ce round"}
    
    # Structure de réponse avec les informations enrichies
    results = []
    for vote in votes:
        user_id = vote['user_id']
        vote_value = vote['vote']
        
        # Récupération des informations utilisateur depuis la collection "users"
        user = users_collection.find_one({"_id": user_id})
        if not user:
            return {"error": f"Utilisateur avec l'ID {user_id} non trouvé"}
        
        username = user.get("username", "Nom inconnu")
        avatar = user.get("avatar", "Avatar non disponible")
        
        # Ajouter les informations dans le résultat final
        results.append({
            "username": username,
            "avatar": avatar,
            "vote_value": vote_value
        })
    
    return results


def strict_round(round_id) -> int:
    """
    Cette fonction permet de valider ou non un round joué en partie strict

    :param round_id: l'identifiant du round
    :param room_code: le code de la room 
    :return : Vrai si la partie est validé, faux sinon.
    
    """
    
    votes = [vote['vote_value'] for vote in get_votes_for_task_in_round(round_id)]
    print(votes)
    if len(set(votes)) == 1 :
        value = votes[0] 
        add_estimation_task(round_id,value)
        return value
    else : 
        return
    


def mean_round(round_id) -> int:
    """
    Cette fonction permet de valider ou non un round joué en partie moyenne

    :param round_id: l'identifiant du round
    :return : l'estimation de la tache.
    
    """
    # On fait le premier round en mode stricte 
    strict_round(round_id)
    # On vérifie si le round est validé (la fonction strict_round va renvoyer l'estimation directement si le round a été validé)
    if strict_round(round_id):
        return strict_round(round_id)
    else:
        # On recupère les votes et on fait la moyenne
        votes = [vote['vote_value'] for vote in get_votes_for_task_in_round(round_id)]
        # Vérifier si "coffee" est dans les votes
        if "coffee" in votes:
            return {"error": "Vote 'coffee' détecté, estimation non calculée"}
        # Convertir les votes en entiers
        votes = [int(vote) for vote in votes]
        # On fait la moyenne puis on arrondi au supérieur pour avoir un entier 
        estimation= round(sum(votes) / len(votes))
        add_estimation_task(round_id,estimation)
        return estimation

def median_round(round_id) -> int:
    """
    Cette fonction permet de valider ou non un round joué en partie médiane

    :param round_id: l'identifiant du round
    :return : l'estimation de la tache.
    
    """
    # On fait le premier round en mode stricte 
    strict_round(round_id)
    # On vérifie si le round est validé (la fonction strict_round va renvoyer l'estimation directement si le round a été validé)
    if strict_round(round_id):
        return strict_round(round_id)
    else:
        # On recupère les votes et on fait la moyenne
        votes = [vote['vote_value'] for vote in get_votes_for_task_in_round(round_id)]
        # Vérifier si "coffee" est dans les votes
        if "coffee" in votes:
            return {"error": "Vote 'coffee' détecté, estimation non calculée"}
        # Convertir les votes en entiers
        votes = [int(vote) for vote in votes]
        votes.sort()
        estimation= votes[len(votes)//2]
        add_estimation_task(round_id,estimation)
        return estimation


def coffee_break(round_id) -> bool:
    """
    Cette fonction permet de déterminer si tous les utilisateurs ont voté pour une pause café

    :param round_id: l'identifiant du round
    :return : Vrai pour partir en pause café, faux sinon
    
    """
    
    votes = [vote['vote_value'] for vote in get_votes_for_task_in_round(round_id)]

<<<<<<< HEAD
    # La même valeur est choisie par tous les utilisateurs et celle-ci est "coffee"
=======
    # La même valeur est choisie par tout les utilisateurs et celle-ci est "café"
>>>>>>> 2b44b8efe1031e3bd6749952993722593a40d99d
    return (len(set(votes)) == 1 and votes[0] == "coffee")

def reveal_votes(round_id, room_code):
    """
    Cette fonction permet de valider une partie.

    :param round_id:
    :param room_code: 
    """
    estimation = None

    game_rule = rooms_collection.find_one(
        {"room_code": room_code}, 
        {"game_rule": 1, "_id": 0} # inclure uniquement game_rule
    )

    game_rule = game_rule["game_rule"]
    
    users = get_users_in_room(room_code)
    votes = [vote['vote_value'] for vote in get_votes_for_task_in_round(round_id)]

    print(len(votes), len(users))
    # Test et ajout de l'estimation
    if len(votes) == len(users):
        
        # Pause café
        if coffee_break(round_id):
            return {"estimated" : True, "estimation" : "coffee"}
        
        match game_rule:
            case "strict":
                estimation = strict_round(round_id)
            case "mean":
                estimation = mean_round(round_id)
            case "median":
                estimation = median_round(round_id)

        if estimation is None :
            return {"estimated" : False, "erreur":"1"}
        else : 
            return {"estimated" : True, "estimation" : estimation}
    else :
        return {"estimated" : False, "erreur":"2"}
    