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

def backlog_json_to_df(backlog_json) -> pd.DataFrame:
    """
    Cette fonction vérifie la structure d'un backlog importé au format JSON et le convertit en DataFrame
    avant insertion en base de données.
    
    :param backlog_json: Chemin du fichier backlog au format JSON.
    :returns DataFrame: Un DataFrame contenant les données si le fichier est bien structuré, sinon un DataFrame vide.
    """
    # Vérification de l'extension du fichier avant de le charger
    
    try:
        # Tentative de chargement du fichier JSON
        backlog_df = pd.read_json(backlog_json)
    except ValueError as e:
        print(f"Erreur : Le fichier JSON est invalide ou corrompu. Détails : {e}")
        return pd.DataFrame()
    except FileNotFoundError:
        print(f"Erreur : Le fichier JSON spécifié est introuvable : {backlog_json}")
        return pd.DataFrame()
    
    # Vérification de la structure du backlog
    expected_columns = ["en_tant_que", "fonctionnalite", "objectif"]
    missing_columns = [col for col in expected_columns if col not in backlog_df.columns]
    if missing_columns:
        print(f"Erreur : Les colonnes suivantes sont manquantes dans le fichier : {', '.join(missing_columns)}")
        return pd.DataFrame()
    
    # Retourne le DataFrame si tout est correct
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
