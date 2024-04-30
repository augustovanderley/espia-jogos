import requests
import os
import sys

from usuarios import usuarios

BASE_URL = 'https://ludopedia.com.br/api/v1/colecao'

token = os.getenv('LUDOPEDIA_ACCESS_TOKEN')

if len(sys.argv) > 1:
    nome_jogo = sys.argv[1]
else:
    print("Favor, inserir o nome de algum jogo ou trecho de nome.")
    sys.exit()

headers = {'Authorization': f'Bearer {token}'}

print(f"Quem tem o jogo com o termo {nome_jogo}?")

for usuario in usuarios:
    params = {
        'id_usuario': usuario.id,
        'lista': 'colecao',
        'ordem': 'nome',
        'tp_jogo': 't',
        'rows': 100,  # Número de resultados por página
        'search': nome_jogo
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code != 200:
        print(f'Erro ao buscar dados: {response.status_code}')

    colecao = response.json()["colecao"]

    
    if colecao:
        print("-------------------------------------")
        print(f"{usuario.nome_legivel}:")
        print("")
        for jogo in colecao:
            nota = jogo["vl_nota"]
            if not nota:
                nota = "-"
            print(f"{jogo["nm_jogo"]} {nota}")

        print("")

