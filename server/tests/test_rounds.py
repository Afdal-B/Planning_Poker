import sys
import os

# Ajout du dossier "server" au chemin de recherche
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from functions.rounds import vote_for_task_in_round, create_round, get_votes_for_task_in_round

# create_round("6754a87dd3da5c9f7dfa40d7","FTR-LYE","120")
#vote_for_task_in_round("6754cda1357f7a9fa9784a23", "6754cd1ff1a3af2e1de53aa6", "5")
round_id = "6754cda1357f7a9fa9784a23"
votes = list(get_votes_for_task_in_round(round_id).values())

pause_cafe = all(element == "café" for element in votes)