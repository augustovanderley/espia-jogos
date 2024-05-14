import json
from dotenv import load_dotenv

from espia_jogos.ludopedia import Ludopedia

load_dotenv(".env")

def update_user_thumbnails(file_path: str):
    # Carregar dados do arquivo JSON
    with open(file_path, 'r') as file:
        users = json.load(file)

    # Atualizar thumbnails faltantes
    for user in users:
        print(user)
        if 'thumb' not in user or not user['thumb']:
            updated_user = Ludopedia.request_user(user['usuario'])
            print(updated_user)
            user['thumb'] = updated_user.get('thumb', '')

    # Salvar os dados atualizados de volta ao arquivo JSON
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)

# Exemplo de uso
update_user_thumbnails('meus_amigos_original.json')