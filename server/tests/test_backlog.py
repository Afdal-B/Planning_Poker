from functions.backlog import backlog_json_to_df
import os
import pytest

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

def test_backlog_invalid_extension():
    """
    Cette fonction permet de tester que les fichiers ayant une extension autre que JSON ne sont pas chargés.
    La fonction fait ce test à partir du fichier "backlog.txt" contenu dans le dossier files
    """
    # Test avec un fichier avec une mauvaise extension
    invalid_extension_file = os.path.join(os.path.dirname(__file__), "files", "backlog.txt")
    df = backlog_json_to_df(invalid_extension_file)
    assert df.empty  # Doit retourner un DataFrame vide