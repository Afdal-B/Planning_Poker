# Application Planning Pocker

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=for-the-badge&logo=render&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

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
### Tester l'application
Vous avez deux options pour tester l'application :  

1. **Version déployée**  
   Accédez à la version déployée de l'application via l'URL suivante :  
   👉 [Planning Poker](https://planning-poker-azure.vercel.app)  

2. **Version locale**  
   Suivez les étapes ci-dessous pour cloner et exécuter l'application localement :

### Étapes pour la version locale
1. Clonez le projet :
   ```bash
   git clone https://github.com/Afdal-B/Planning_Poker.git
   cd <nom_du_repo>

2. Installez les dépendances :
    * Pour le frontend
        ```bash
        cd client 
        npm install

    * Pour le backend
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        pip install -r requirements.txt

3. Lancer l'application :
    * Pour le frontend 
        ```bash
        npm start 
    * Pour le backend 
        ```bash
        python main.py  

## Documentation 
### Frontend
La documentation du frontend a été générée automatiquement à l'aide de scripts npm. Elle se trouve dans le dossier [`client/docs`](client/docs) Pour y accéder :

* Clonez le projet en local.
* Explorez les fichiers disponibles dans le dossier client/docs pour consulter les détails des composants, des hooks et des fonctionnalités du frontend.

### Backend 
La documentation du backend a été générée automatiquement avec Sphinx. Elle est disponible dans le dossier [`server/docs/_build/html`](server/docs/_build/html). Pour y accéder :

* Clonez le projet en local.
* Ouvrez le fichier index.html situé dans le dossier server/docs/_build/html avec votre navigateur.
* Consultez les instructions détaillées pour les API et les configurations du backend.


## Les contributeurs

- Afdal BOURAIMA
- Yousra BOUHANNA
- Elias AIT HASSOU

## Licence

Aucune licence spécifique n'a encore été attribuée à ce projet. Tous les droits sont réservés par les contributeurs. Si vous souhaitez utiliser ou modifier ce projet, veuillez contacter les contributeurs pour obtenir leur autorisation.
