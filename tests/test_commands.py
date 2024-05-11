import pytest
from typer.testing import CliRunner

from espia_jogos.usuarios import Usuario
from espia_jogos.main import app

runner = CliRunner()


@pytest.fixture
def mock_usuarios(monkeypatch):
    def load_usuarios_from_json(caminho_arquivo):
        return [
            Usuario(id_usuario=123, usuario='johndoe', nome_legivel='John Doe', thumb='path/to/thumb1.jpg'),
            Usuario(id_usuario=456, usuario='janedoe', nome_legivel='Jane Doe', thumb='path/to/thumb2.jpg')
        ]
    monkeypatch.setattr('espia_jogos.main.load_usuarios_from_json', load_usuarios_from_json)


@pytest.fixture
def mock_ludopedia(monkeypatch):
    def request_collection(user_id, game_name):
        return [{'nm_jogo': 'Catan', 'vl_nota': 5}]

    def request_users(user_search):
        return [{'id_usuario': '123', 'usuario': 'johndoe'}]

    monkeypatch.setattr('espia_jogos.ludopedia.Ludopedia.request_collection', request_collection)
    monkeypatch.setattr('espia_jogos.ludopedia.Ludopedia.request_users', request_users)


@pytest.fixture
def mock_scraper(monkeypatch):
    def usuarios_do_grupo(group_id):
        return ['user1', 'user2']

    monkeypatch.setattr('espia_jogos.scraper.Scraper.usuarios_do_grupo', usuarios_do_grupo)


def test_jogos(mock_usuarios, mock_ludopedia):
    result = runner.invoke(app, ['jogos', 'catan'])
    assert result.exit_code == 0
    assert 'Quem tem o jogo com o termo catan?' in result.stdout
    assert 'John Doe' in result.stdout
    assert 'Catan 5' in result.stdout


def test_usuario(mock_ludopedia):
    result = runner.invoke(app, ['usuario', 'johndoe'])
    assert '"usuario": "johndoe"' in result.stdout

def test_extrai_grupo(mocker):
    mocker.patch('espia_jogos.main.carrega_dados_de_grupo_de_usuarios', return_value=[{"id_usuario": 1, "usuario": "User1", "thumb": "lalalala"}])
    mock_write = mocker.patch('espia_jogos.main.escreve_dados_usuarios')

    result = runner.invoke(app, ['extrai-grupo', '123'])
    assert result.exit_code == 0

    mock_write.assert_called_once()