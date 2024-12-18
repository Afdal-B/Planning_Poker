"""
Ce module regroupe l'ensemble des fonctions permettant d'intéragir avec le backlog.
"""

import pandas as pd
from bson import ObjectId
import json
from pymongo.mongo_client import MongoClient


client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']
tasks_collection = db['tasks']

import pandas as pd

def backlog_json_to_df(backlog_json) -> pd.DataFrame:
    """
    Cette fonction vérifie la structure d'un backlog importé au format JSON et le convertit en DataFrame
    avant insertion en base de données. Elle accepte deux structures :
    1. 3 colonnes : ["en_tant_que", "fonctionnalite", "objectif"]
    2. 4 colonnes : ["en_tant_que", "fonctionnalite", "objectif", "estimation"] (backlog temporaire)
    
    :param backlog_json: Le contenu du fichier JSON.
    :returns DataFrame: Un DataFrame contenant les données si le fichier est bien structuré, sinon un DataFrame vide.
    """
    try:
        # Tentative de chargement du fichier JSON
        backlog_df = pd.read_json(backlog_json)
    except ValueError as e:
        print(f"Erreur : Le fichier JSON est invalide ou corrompu. Détails : {e}")
        return pd.DataFrame()
    except FileNotFoundError:
        print(f"Erreur : Le fichier JSON spécifié est introuvable : {backlog_json}")
        return pd.DataFrame()

    # Vérification de la structure du backlog : soit 3 colonnes, soit 4 colonnes
    expected_columns_3 = ["en_tant_que", "fonctionnalite", "objectif"]
    expected_columns_4 = expected_columns_3 + ["estimation"]

    # Vérifier si le fichier a 3 ou 4 colonnes
    if backlog_df.columns.equals(pd.Index(expected_columns_3)):
        # Structure avec 3 colonnes
        print("Structure du backlog : 3 colonnes détectées.")
    elif backlog_df.columns.equals(pd.Index(expected_columns_4)):
        # Structure avec 4 colonnes
        print("Structure du backlog : 4 colonnes détectées.")
    else:
        print("Erreur : Le fichier JSON ne correspond ni à la structure à 3 ni à la structure à 4 colonnes.")
        return pd.DataFrame()

    # Retourne le DataFrame si la structure est valide
    return backlog_df

def export_backlog_to_json(room_code):
    """
    Exporte les colonnes "en_tant_que", "fonctionnalite", "objectif" et "estimation"
    pour un room_code donné dans un fichier JSON.
    """
    
    try:
        # Récupération des tâches pour le room_code donné
        tasks = list(tasks_collection.find(
            {"room_code": room_code}, 
            {"_id": 0, "en_tant_que": 1, "fonctionnalite": 1, "objectif": 1, "estimation": 1}
        ))
        
        if not tasks:
            print(f"Aucune tâche trouvée pour le room_code: {room_code}")
            return

        # Écriture des données dans un fichier JSON
        with open("backlog_temporaire.json", "w", encoding="utf-8") as json_file:
            json.dump(tasks, json_file, ensure_ascii=False, indent=4)

        print(f"Les tâches ont été exportées dans 'backlog_temporaire.json'.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

def upload_backlog(backlog_df, room_code)->list: 
    """
    Cette fonction permet d'uploader un backlog importé au format JSON et et insère chaque tâche dans la base de données MongoDB.
    Le backlog doit contenir 3 champs par tâche : "En tant que", "Fonctionnalité" et "Objectif".

    :param backlog: DataFrame contenant le backlog à uploader.
    :type backlog_json: pd.DataFrame
    :param room_code: Code la room dans laquelle le backlog est chargé

    :return task_ids: renvoie la liste des id des tâches chargées depuis le backlog
    """

    # Liste des tâches du backlog
    task_ids = []

    if not backlog_df.empty :
        # Récupération et insertion de chaque tâche en base de données
        for _,task in backlog_df.iterrows():
            task_document = {
                "_id": str(ObjectId()),
                "room_code": room_code,
                "en_tant_que": task.get("en_tant_que"),
                "fonctionnalite": task.get("fonctionnalite"),
                "objectif": task.get("objectif"),
                "estimation": None,
                "rounds": []
            }

            try:
                tasks_collection.insert_one(task_document)
                task_ids.append(task_document["_id"])
            except Exception as e:
                print(f"Erreur lors de l'insertion du document: {e}")
        return task_ids
    return []

def next_task(room_code):
    """
    Récupère la prochaine tâche sans estimation pour une room spécifique, triée par ordre alphabétique
    du champ 'fonctionnalite'.

    :param room_code (str): Code de la room.

    Returns:
        dict: La tâche trouvée ou None si aucune tâche correspondante.
    """

    # Requête pour trouver la première tâche sans estimation pour la room
    task = tasks_collection.find_one(
        {
            "room_code": room_code,   
            "estimation": None      
        },
        sort=[("fonctionnalite", 1)]  # Tri par ordre alphabétique pour s'assurer de l'ordre de renvoi des tâches
    )

    return task


def get_all_tasks(room_code):
    """
    Récupère toutes les tâches pour une room spécifique, sans tri.

    :param room_code (str): Code de la room.

    Returns:
        list: Une liste de toutes les tâches correspondant aux critères.
    """

    # Requête pour trouver toutes les tâches pour la room
    tasks = list(tasks_collection.find(
        {
            "room_code": room_code
        }
    ))

    return tasks


def add_estimation_task(task_id,value):
    """
    Met à jour le champ 'estimation' d'une tâche spécifique après validation du vote

    
    :param value: La valeur de l'estimation à ajouter
    :param task_id: L'identifiant unique de la tâche dans MongoDB

    Returns:
        dict: Le document mis à jour s'il a été trouvé et modifié.
        None: Si aucun document correspondant n'a été trouvé.
    """
    try:
        
        # Mise à jour de la tâche
        result = tasks_collection.find_one_and_update(
            {"_id": task_id},  # Filtre pour trouver la tâche
            {"$set": {"estimation": value}},  # Mise à jour du champ estimation
            return_document=True  # Retourne le document mis à jour
        )
        return result  # Retourne la tâche mise à jour ou None si non trouvée

    except Exception as e:
        print(f"Erreur lors de la mise à jour de la tâche : {e}")
        return None
    
