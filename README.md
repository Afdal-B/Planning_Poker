# Application planning pocker

## Présentation du projet
L'application **Planning Poker** est un outil collaboratif pour les équipes agiles, permettant d'estimer la difficulté des tâches d'un projet à l'aide de cartes virtuelles. Elle offre une interface simple pour créer des sessions et voter sur les tâches. Une fonctionnalité de chat en temps réel est également intégrée, permettant aux membres de l'équipe de communiquer, discuter des estimations et parvenir rapidement à un consensus.

### fonctionnalités principales
- **Création de sessions** :  
  Les utilisateurs peuvent créer de nouvelles sessions,pour estimer les tâches d'un projet en choisissant une règle parmi *strict*, *médiane* et *moyenne*.  

- **Vote en temps réel** :  
  Les membres de l'équipe participent à l'estimation des tâches en utilisant des cartes virtuelles, et les résultats sont affichés en temps réel, garantissant une transparence et une collaboration optimales.  

- **Chat en temps réel** :  
  Une messagerie intégrée permet aux participants de communiquer facilement, discuter des estimations et atteindre rapidement un consensus.  

- **Support pour reprise après une pause** :  
  Les sessions peuvent être suspendues, sauvegardées et reprises ultérieurement, permettant une planification flexible sans perte de données.  


## Technologies utilisées

- Frontend : React
- Backend : Flask (Python)
- Base de données : MongoDB
- Intégration continue: Github Actions
- Déploiment continu: Render et Vercel

## Pipeline CI/CD
Le projet utilise GitHub Actions pour automatiser le processus d'intégration. Les workflows sont configurés pour s'exécuter à chaque push sur la branche main et lors des pull requests. Ces actions automatisent des tâches essentielles comme la récupération du code, l'installation des dépendances, l'exécution des tests, la génération de la documentation.

Le déploiement continu a été mis en place en utilisant :  
- **Render** pour le backend,  
- **Vercel** pour le frontend.  

Ces plateformes sont connectées directement au dépôt GitHub, ce qui garantit que chaque mise à jour validée sur la branche principale est automatiquement déployée sur les environnements correspondants.  

La configuration des pipelines CI/CD se trouve dans les fichiers `CI.yaml` et `test.yml` dans le répertoire [`.github/workflows`](.github/workflows).

## Installation 
1. Clonez le projet :
   ```bash
   git clone https://github.com/Afdal-B/Planning_Poker.git

2. Installez les dépendances :
    * Pour le frontend 
        npm install

    * Pour le backend
        pip install -r requirements.txt

3. Lancer l'application :
    * Pour le frontend 
        npm start 
    * Pour le backend 
        flask run 

## Documentation 




## Les contributeurs

- Afdal BOURAIMA
- Yousra BOUHANNA
- Elias AIT HASSOU
