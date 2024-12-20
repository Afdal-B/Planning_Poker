from functions.backlog import backlog_json_to_df
import os
import pytest
import pandas as pd

def test_backlog_valid():
    """
    Cette fonction permet de tester que les fichiers JSON avec une structure valide sont chargés.
    La fonction fait ce test à partir du fichier "backlog_valid.json" contenu dans le dossier files
    """
    # Test avec un fichier valide
    valid_file = os.path.join(os.path.dirname(__file__), "files", "backlog_valid.json")

    df = backlog_json_to_df(valid_file)
    assert not df.empty  # Vérifie que le DataFrame n'est pas vide
    assert list(df.columns) == ["en_tant_que", "fonctionnalite", "objectif"]  # Colonnes attendues

def test_backlog_invalid_structure():
    """
    Cette fonction permet de tester que les fichiers JSON avec une structure invalide ne sont pas chargés.
    La fonction fait ce test à partir du fichier "backlog_invalid.json" contenu dans le dossier files
    """
    # Test avec un fichier JSON invalide
    invalid_file = os.path.join(os.path.dirname(__file__), "files", "backlog_invalid.json")
    df = backlog_json_to_df(invalid_file)
    assert df.empty  # Doit retourner un DataFrame vide

def test_backlog_tmp_structure():
    """
    Cette fonction teste la structure du fichier JSON temporaire renvoyé lorsque les utilisateurs vont en pause.
    """
    
    tmp_file = os.path.join(os.path.dirname(__file__), "files", "backlog_temporaire.json")
    df = backlog_json_to_df(tmp_file)
    
    # Vérifications
    assert not df.empty  # Vérifie que le DataFrame n'est pas vide
    assert list(df.columns) == ["en_tant_que", "fonctionnalite", "objectif", "estimation"]  # Colonnes attendues