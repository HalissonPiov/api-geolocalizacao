from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_adicionar_e_listar_ponto():
    # Cria o usuário
    response_user = client.post("/AdicionarUsuario/?email=ponto@example.com&nome=Usuário Ponto")
    assert response_user.status_code == 200
    usuario_id = response_user.json()["id"]

    # Adiciona ponto
    response_add = client.post(
        f"/AdicionarPonto/?usuario_id={usuario_id}&latitude=-23.55&longitude=-46.63&descricao=Parque Central"
    )
    assert response_add.status_code == 200
    assert "Ponto adicionado com sucesso" in response_add.text

    # Lista pontos
    response_list = client.get(f"/ListarPontosPorUsuario/?usuario_id={usuario_id}")
    assert response_list.status_code == 200
    assert any(ponto["descricao"] == "Parque Central" for ponto in response_list.json())
