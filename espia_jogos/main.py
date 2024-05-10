from pathlib import Path

import json
import typer

from espia_jogos.usuarios import usuarios
from espia_jogos.ludopedia import Ludopedia
from espia_jogos.scraper import Scraper

app = typer.Typer()


@app.callback()
def callback():
    """
    Espia Jogos dos Amigos
    """


@app.command()
def jogos(nome_jogo: str) -> None:
    print(f"Quem tem o jogo com o termo {nome_jogo}?")
    for usuario in usuarios:
        colecao = Ludopedia.request_collection(usuario.id_usuario, nome_jogo)
        print_collection(usuario, colecao)


@app.command()
def usuario(usuario_procurado: str) -> None:
    usuarios = Ludopedia.request_users(usuario_procurado)
    for usuario in usuarios:
        if usuario["usuario"].lower() == usuario_procurado.lower():
            print_usuario(usuario)
            break


@app.command()
def extrai_grupo(grupo: int, overwrite=True) -> None:
    usuarios = Scraper.usuarios_do_grupo(grupo)

    dados_usuario = []
    for usuario in usuarios:
        dados_usuario.extend(Ludopedia.request_users(usuario))

    output_path = Path("meus_amigos.json")

    if output_path.exists() and not overwrite:
        with open(output_path, "r") as file:
            dados_usuario.extend(json.loads(file.read()))

    with open(output_path, "w") as file:
        file.write(json.dumps(dados_usuario, indent=4))


def print_collection(usuario: str, colecao: list[str]) -> None:
    if colecao:
        print("-" * 20)
        print(f"{usuario.usuario}:")
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


if __name__ == "__main__":
    app()
