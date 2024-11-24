import string, random
def verify_exist_room_code(room_code)->bool:
    """
    Cette fonction vérifie l'unicité des code rooms qui sont générés aléatoirement.
    La fonction retourne True si le room_code existe en base de données, False sinon.

    :param room_code: Code la room à vérifier
    """
    existing_room = db.rooms.find_one({'code': room_code})
    if existing_room:
        return True
    else:
        return False  

def generate_room_code()->str:
    """
    Cette fonction génère un code d'accès à une room de 6 caractères. Le code suivra la structure suivante : XXX-XXX
    """
    characters = string.ascii_letters + string.digits
    while True:
        room_code = ''.join(random.choice(characters) for _ in range(6))
        room_code = room_code[:3] + '-' + room_code[3:]
        room_code = str.upper(room_code)
        if not verify_exist_room_code(room_code):
            return room_code