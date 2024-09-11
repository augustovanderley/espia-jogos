import json
from pathlib import Path
import typer
from typing import List

from espia_jogos.usuarios import load_usuarios_from_json, carrega_dados_de_grupo_de_usuarios, escreve_dados_usuarios
from espia_jogos.ludopedia import Ludopedia

app = typer.Typer()

OUTPUT_CAMINHO_ARQUIVO = Path("meus_amigos.json")

@app.callback()
def callback():
    """
    Espia Jogos dos Amigos
    """


@app.command()
def jogos(nome_jogo: str) -> None:
    print(f"Quem tem o jogo com o termo {nome_jogo}?")
    for usuario in load_usuarios_from_json("meus_amigos.json"):
        colecao = Ludopedia.request_collection(usuario.id_usuario, nome_jogo)
        print_collection(usuario, colecao)


@app.command()
def usuario(usuario_procurado: List[str]) -> None:
    for nome in usuario_procurado:
        usuarios = Ludopedia.request_users(nome)
        for usuario in usuarios:
            if usuario["usuario"].lower() == nome.lower():
                print_usuario(usuario)
                break



@app.command()
def extrai_grupo(id_grupo: int, overwrite=True, caminho_output : Path = OUTPUT_CAMINHO_ARQUIVO) -> None:
    try:
        dados_usuario = carrega_dados_de_grupo_de_usuarios(id_grupo)
        escreve_dados_usuarios(dados_usuario, caminho_output, overwrite)
    except Exception as e:
        print(f"An error occurred: {e}")


def print_collection(usuario: str, colecao: list[str]) -> None:
    if colecao:
        print("-" * 20)
        name_to_display = usuario.nome_legivel if usuario.nome_legivel else usuario.usuario
        print(f"{name_to_display}:")
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
        "thumb": usuario["thumb"],
        "priority_search": "false",
    }
    print(json.dumps(informacao, indent=4))


if __name__ == "__main__":
    app()
