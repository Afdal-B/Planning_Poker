import sys
import os

# Ajout du dossier "server" au chemin de recherche
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from functions.users import create_user

create_user("AdfalBOU", "link.jpg", "FTR-LYE")  