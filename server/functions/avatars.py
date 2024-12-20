from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']
avatars_collection = db['avatars']  # Nom de la collection

def get_avatars()->list:
    """
    Cette fonction permet de retourner tout les avatars initialement stockés en base de données pour permettre à l'utilisateur d'en choisir un.
    """