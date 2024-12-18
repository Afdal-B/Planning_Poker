from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb+srv://aithassouelias57:xBG54MaCnybEuSTk@cluster0.85fua.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['planning_poker']
avatars_collection = db['avatars']  # Nom de la collection

# Liste des avatars à insérer
avatars = [
    {
        "url": "https://www.apple.com/newsroom/images/r8-landing-page-tiles/Lion_Animoji_LP_hero.jpg.og.jpg",
        "desc": "Lion"
    },
    {
        "url": "https://emojis.wiki/thumbs/emojis/polar-bear.webp",
        "desc": "Bear"
    },
    {
        "url": "https://emojis.wiki/thumbs/emojis/tiger-face.webp",
        "desc": "Tiger"
    },
    {
        "url": "https://static.tiktokemoji.com/202409/12/X1Cj7fxY.webp",
        "desc": "Tiger2"
    },
    {
        "url": "https://attic.sh/7zqgmqr9ishrlrxdxwmox2n8ja1w",
        "desc": "Dog"
    }
]

# Insérer les avatars dans la collection "avatars"
avatars_collection.insert_many(avatars)

print("Les avatars ont été insérés avec succès dans la base de données.")