import os

import requests
from dotenv import load_dotenv


load_dotenv(".env")


class Ludopedia:
    base_url = "https://ludopedia.com.br/api/v1"
    headers = {"Authorization": f"Bearer {os.getenv("LUDOPEDIA_ACCESS_TOKEN")}"}

    @classmethod
    def request_collection(cls, id_usuario: str, nome_jogo: str) -> list[str]:
        endpoint = f"{cls.base_url}/colecao"
        params = {
            "id_usuario": id_usuario,
            "lista": "colecao",
            "ordem": "nome",
            "tp_jogo": "t",
            "rows": 100,  # Número de resultados por página
            "search": nome_jogo,
        }
        response = requests.get(endpoint, headers=cls.headers, params=params)
        if response.status_code != 200:
            print(f"Erro ao buscar dados: {response.status_code}")
            return []
        return response.json()["colecao"]

    @classmethod
    def request_users(cls, usuario_procurado: str) -> dict[str, str]:
        endpoint = f"{cls.base_url}/usuarios"
        params = {
            "search": usuario_procurado,
        }
        response = requests.get(endpoint, headers=cls.headers, params=params)
        if response.status_code != 200:
            print(f"Erro ao buscar dados: {response.status_code}")
            return []
        return response.json()["usuarios"]
