import json

import click

from .usuarios import usuarios
from .ludopedia import Ludopedia


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("nome_jogo")
def jogos(nome_jogo: str) -> None:

    print(f"Quem tem o jogo com o termo {nome_jogo}?")
    for usuario in usuarios:
        colecao = Ludopedia.request_collection(usuario.id, nome_jogo)
        print_collection(usuario, colecao)


@main.command()
@click.argument("usuario_procurado")
def usuario(usuario_procurado: str) -> None:
    usuarios = Ludopedia.request_users(usuario_procurado)
    for usuario in usuarios:
        if usuario["usuario"].lower() == usuario_procurado.lower():
            print_usuario(usuario)
            break


def print_collection(usuario: str, colecao: list[str]) -> None:
    if colecao:
        print("-" * 20)
        print(f"{usuario.nome_legivel}:")
        print("")
        for jogo in colecao:
            nota = jogo["vl_nota"]
            print(f"{jogo['nm_jogo']} {nota if nota is not None else '-'}")

        print("")


def print_usuario(usuario: str) -> None:
    informacao = {
        "id": usuario["id_usuario"],
        "usuario": usuario["usuario"],
        "nome_legivel": "INSIRA NOME LEGIVEL",
    }
    print(json.dumps(informacao, indent=4))
