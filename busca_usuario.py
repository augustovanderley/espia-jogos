import json
import requests
import os
import sys

token = os.getenv('LUDOPEDIA_ACCESS_TOKEN')

if len(sys.argv) > 1:
    usuario_procurado = sys.argv[1]
else:
    print("Favor, inserir o exato do usuario que está buscando.")
    sys.exit()

base_url = 'https://ludopedia.com.br/api/v1/usuarios'
headers = {'Authorization': f'Bearer {token}'}
params = {
    'search': usuario_procurado,
}

response = requests.get(base_url, headers=headers, params=params)
if response.status_code != 200:
    print(f'Erro ao buscar dados: {response.status_code}')


for usuario in response.json()["usuarios"]:
    if usuario["usuario"].lower() == usuario_procurado.lower():
        informacao = {
            "id": usuario["id_usuario"],
            "usuario": usuario["usuario"],
            "nome_legivel": "INSIRA NOME LEGIVEL",
        }
        print(json.dumps(informacao, indent=4))
        break