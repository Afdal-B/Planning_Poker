import pandas as pd

def backlog_json_to_df(backlog_json)->pd.DataFrame:
    """
    Cette fonction permet de vérifier la structure d'un backlog importé au format JSON et le convertir en DataFrame
    avant insertion en base de données
    :param backlog_json: Backlog au format JSON.
    :returns backlog_df: Backlog au format DataFrame si ce dernier est bien structuré.
    """
    # Vérification du type de fichier importé
    backlog_df = pd.read_json(backlog_json)
    
    if not backlog_json.lower().endswith('.json'):
        print("Erreur : Le fichier importé n'est pas un fichier JSON.")
        return pd.DataFrame()
    
    # Vérification de la structure du backlog
    expected_columns = ["en_tant_que", "fonctionnalite", "objectif"]
    missing_columns = [col for col in expected_columns if col not in backlog_df.columns]
    if missing_columns:
        print(f"Erreur : Les colonnes suivantes sont manquantes dans le fichier : {', '.join(missing_columns)}")
        return pd.DataFrame()
    
    return backlog_df