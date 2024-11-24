import pandas as pd

def backlog_json_to_df(backlog_json) -> pd.DataFrame:
    """
    Cette fonction vérifie la structure d'un backlog importé au format JSON et le convertit en DataFrame
    avant insertion en base de données.
    
    :param backlog_json: Chemin du fichier backlog au format JSON.
    :returns DataFrame: Un DataFrame contenant les données si le fichier est bien structuré, sinon un DataFrame vide.
    """
    # Vérification de l'extension du fichier avant de le charger
    if not backlog_json.lower().endswith('.json'):
        print("Erreur : Le fichier importé n'est pas un fichier JSON.")
        return pd.DataFrame()
    
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
