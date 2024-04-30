import requests
import os
import json

import click
from dotenv import load_dotenv

from .usuarios import usuarios


@click.group()
def main():
    pass


@main.command()
@click.argument("nome_jogo")
def jogos(nome_jogo):
    token = load_token()

    print(f"Quem tem o jogo com o termo {nome_jogo}?")

    for usuario in usuarios:
        colecao = request_collection(usuario.id, nome_jogo, token)
        print_collection(usuario, colecao)


@main.command()
@click.argument("usuario_procurado")
def usuario(usuario_procurado):
    token = load_token()
    usuarios = request_users(usuario_procurado, token)

    for usuario in usuarios:
        if usuario["usuario"].lower() == usuario_procurado.lower():
            print(usuario)
            break


def load_token():
    load_dotenv(".env")
    return os.getenv("LUDOPEDIA_ACCESS_TOKEN")


def print_collection(usuario, colecao):
    if colecao:
        print("-------------------------------------")
        print(f"{usuario.nome_legivel}:")
        print("")
        for jogo in colecao:
            nota = jogo["vl_nota"]
            if not nota:
                nota = "-"
            print(f"{jogo['nm_jogo']} {nota}")

        print("")


def print_usuario(usuario):
    informacao = {
        "id": usuario["id_usuario"],
        "usuario": usuario["usuario"],
        "nome_legivel": "INSIRA NOME LEGIVEL",
    }
    print(json.dumps(informacao, indent=4))


def request_collection(id_usuario, nome_jogo, token):
    BASE_URL = "https://ludopedia.com.br/api/v1/colecao"

    token = load_token()
    headers = {"Authorization": f"Bearer {token}"}

    params = {
        "id_usuario": id_usuario,
        "lista": "colecao",
        "ordem": "nome",
        "tp_jogo": "t",
        "rows": 100,  # Número de resultados por página
        "search": nome_jogo,
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Erro ao buscar dados: {response.status_code}")
        return []

    colecao = response.json()["colecao"]

    return colecao


def request_users(usuario_procurado, token):
    token = load_token()
    base_url = "https://ludopedia.com.br/api/v1/usuarios"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "search": usuario_procurado,
    }

    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Erro ao buscar dados: {response.status_code}")
        return []
    return response.json()["usuarios"]
