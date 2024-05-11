from dataclasses import dataclass, field
from pathlib import Path
from typing import List
import json

from espia_jogos.scraper import Scraper
from espia_jogos.ludopedia import Ludopedia


@dataclass
class Usuario:
    id_usuario: int
    usuario: str
    nome_legivel: str = field(default='')
    thumb: str = field(default='')


def load_usuarios_from_json(file_path: str) -> list[Usuario]:
    with open(file_path, "r") as file:
        data = json.load(file)
        return [Usuario(**item) for item in data]

def carrega_dados_de_grupo_de_usuarios(id_grupo: int) -> List[dict]:
    usuarios = Scraper.usuarios_do_grupo(id_grupo)
    dados_usuario = []
    for usuario in usuarios:
        dados_usuario.extend(Ludopedia.request_users(usuario))
    return dados_usuario


def escreve_dados_usuarios(dados_usuario: List[dict], caminho_output: Path, overwrite: bool):
    if caminho_output.exists() and not overwrite:
        with open(caminho_output, "r") as file:
            dados_existentes = json.loads(file.read())
            dados_usuario.extend(dados_existentes)

    with open(caminho_output, "w") as file:
        file.write(json.dumps(dados_usuario, indent=4))

