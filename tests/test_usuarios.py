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

def test_criar_usuario():
    response = client.post("/AdicionarUsuario/?email=usuario_unico@example.com&nome=Usuário Teste")
    data = response.json()
    assert response.status_code == 200
    assert data["email"] == "usuario_unico@example.com"
    assert data["nome"] == "Usuário Teste"

def test_remover_usuario():
    # Primeiro, cria o usuário
    client.post("/AdicionarUsuario/?email=remover@example.com&nome=Remover")

    # Em seguida, remove
    response = client.delete("/RemoverUsuario/?email=remover@example.com")
    data = response.json()
    assert response.status_code == 200
    assert data["msg"] == "Usuário removido"

