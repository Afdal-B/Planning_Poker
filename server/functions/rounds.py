"""
Ce module regroupe l'ensemble des fonctions permettant d'intéragir avec les rounds d'une partie de Planning Pocker.
"""

from bson import ObjectId
from pymongo.mongo_client import MongoClient
from datetime import datetime
from .backlog import next_task, add_estimation_task

client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']

# Création des collections
rooms_collection = db['rooms']
tasks_collection = db['tasks']
rounds_collection = db['rounds']

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
    
    # Vérification si le round est actif
    if not round['is_active']:
        return {"error": "Le round n'est plus actif, impossible de voter"}
    
    # Vérification si l'utilisateur a déjà voté
    existing_vote = next((vote for vote in round['votes'] if vote['user_id'] == user_id), None)
    if existing_vote:
        return {"error": "L'utilisateur a déjà voté"}
    
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
    Récupère l'ensemble des votes pour une tâche spécifique dans un round. 
    
    :param round_id: L'ID du round pour lequel récupérer les votes.
    :return: Un dictionnaire contenant la liste des votes par utilisateur ou un message d'erreur.
    """
    
    # Recherche du round dans la base de données
    round = rounds_collection.find_one({"_id": round_id})
    if not round:
        return {"error": "Round non trouvé"}
    
    # Vérification si des votes existent
    votes = round.get("votes", [])
    if not votes:
        return {"error": "Aucun vote trouvé pour ce round"}
    
    # Structure de réponse avec les votes par utilisateur
    results = {}
    for vote in votes:
        user_id = vote['user_id']
        vote_value = vote['vote']
        voted_at = vote['voted_at']
        
        if user_id not in results:
            results[user_id] = []
        results.update({user_id: vote_value})
    
    return results

def strict_round(round_id) -> bool:
    """
    Cette fonction permet de valider ou non un round joué en partie strict

    :param round_id: l'identifiant du round
    :return : Vrai si la partie est validé, faux sinon.
    
    """
    
    votes = list(get_votes_for_task_in_round(round_id).values())

    # Test et ajout de l'estimation
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
    #On fait le premier round en mode stricte 
    strict_round(round_id)
    #On vérifie si le round est validé (la fonction strict_round va renvoyer l'estimation directement si le round a été validé)
    if strict_round(round_id):
        return strict_round(round_id)
    else:
        #On recupère les votes et on fait la moyenne
        votes = list(get_votes_for_task_in_round(round_id).values())
        #On fait la moyenne puis on arrondi au supérieur pour avoir un entier 
        return round(sum(votes)/len(votes))

def median_round(round_id) -> int:
    """
    Cette fonction permet de valider ou non un round joué en partie médiane

    :param round_id: l'identifiant du round
    :return : l'estimation de la tache.
    
    """
    #On fait le premier round en mode stricte 
    strict_round(round_id)
    #On vérifie si le round est validé (la fonction strict_round va renvoyer l'estimation directement si le round a été validé)
    if strict_round(round_id):
        return strict_round(round_id)
    else:
        #On recupère les votes et on fait la moyenne
        votes = list(get_votes_for_task_in_round(round_id).values())
        votes.sort()
        return votes[len(votes)//2]
    

def coffee_break(round_id) -> bool:
    """
    Cette fonction permet de déterminer si tous les utilisateurs ont voté pour une pause café

    :param round_id: l'identifiant du round
    :return : Vrai pour partir en pause café, faux sinon
    
    """
    
    votes = list(get_votes_for_task_in_round(round_id).values())

    # La même valeur est choisie par tout les utilisateurs et celle-ci est "café"
    return (len(set(votes)) == 1 and votes[0] == "café")

def reveal_votes(round_id, room_code):
    """
    Cette fonction permet de jouer une partie à partir
    """
    game_rule = rooms_collection.find_one(
        {"room_code": room_code}, 
        {"game_rule": 1, "_id": 0} # inclure uniquement game_rule
    )

    # Pause café
    if coffee_break(round_id):
        return "coffee break"
    
    match game_rule:
        case "strict":
            strict_round(round_id)
        case "mean":
            mean_round(round_id)
        case "median":
            median_round(round_id)

    # Chercher la prochaine tâche
    task = next_task(room_code)

    # Si il n'y pas de prochaine tâche la partie est terminée, sinon renvoyer la tâche
    if task is None :
        return 
    else : 
        return task

    

