from functions.backlog import backlog_json_to_df
import os
import pytest

def test_backlog_valid():
    """
    Cette fonction teste
    """
    # Test avec un fichier valide
    valid_file = os.path.join('/', 'server', 'test', 'files', 'backlog_valid.json')

    df = backlog_json_to_df(valid_file)
    assert not df.empty  # Vérifie que le DataFrame n'est pas vide
    assert list(df.columns) == ["en_tant_que", "fonctionnalite", "objectif"]  # Colonnes attendues

def test_backlog_invalid_structure():
    """
    """
    # Test avec un fichier JSON invalide
    invalid_file = os.path.join('/', 'server', 'test', 'files', 'backlog_invalid.json')
    df = backlog_json_to_df(invalid_file)
    assert df.empty  # Doit retourner un DataFrame vide

def test_backlog_invalid_extension():
    """
    """
    # Test avec un fichier avec une mauvaise extension
    invalid_extension_file = os.path.join('/', 'server', 'test', 'files', 'backlog.txt')
    df = backlog_json_to_df(invalid_extension_file)
    assert df.empty  # Doit retourner un DataFrame vide