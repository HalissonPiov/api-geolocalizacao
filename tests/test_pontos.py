import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SQLModel, engine

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Limpa e recria as tabelas do banco de dados antes de cada teste
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)

def test_adicionar_e_listar_ponto():
    # Cria o usuário associado ao ponto
    res_usuario = client.post("/AdicionarUsuario/?email=ponto@example.com&nome=Usuário Ponto")
    usuario_id = res_usuario.json()["id"]

    # Adiciona ponto para o usuário
    response_add = client.post(
        f"/AdicionarPonto/?usuario_id={usuario_id}&descricao=Parque Central&latitude=-23.55&longitude=-46.63"
    )
    assert response_add.status_code == 200
    assert "Ponto adicionado com sucesso" in response_add.text

    # Lista os pontos
    response_list = client.get("/ListarPontos/")
    assert response_list.status_code == 200
    assert "Parque Central" in response_list.text

