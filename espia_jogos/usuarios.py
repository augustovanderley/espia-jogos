from dataclasses import dataclass, field
import json


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


usuarios = load_usuarios_from_json("meus_amigos.json")
