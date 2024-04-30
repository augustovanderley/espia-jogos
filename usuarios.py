from dataclasses import dataclass
import json

@dataclass
class Usuario:
    id: int
    usuario: str
    nome_legivel: str

def load_usuarios_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Usuario(**item) for item in data]

usuarios = load_usuarios_from_json("meus_amigos.json")