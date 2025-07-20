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

def test_atualizar_ponto():
    # Cria usuário
    usuario_resp = client.post("/AdicionarUsuario/", params={"nome": "Usuario Ponto", "email": "ponto@example.com"})
    usuario_id = usuario_resp.json()["id"]

    # Adiciona ponto geográfico
    ponto_resp = client.post("/AdicionarPonto/", params={
        "usuario_id": usuario_id,
        "latitude": -23.55,
        "longitude": -46.63,
        "descricao": "Ponto Inicial"
    })
    ponto_id = ponto_resp.json()["ponto"]["id"]

    # Atualiza o ponto
    response = client.put("/AtualizarPonto/", params={
        "ponto_id": ponto_id,
        "usuario_id": usuario_id,
        "nova_latitude": -22.9,
        "nova_longitude": -43.2,
        "nova_descricao": "Ponto Atualizado"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["latitude"] == -22.9
    assert data["longitude"] == -43.2
    assert data["descricao"] == "Ponto Atualizado"

def test_remover_ponto():
    # Criação de um usuário para associar o ponto
    response_usuario = client.post(
        "/AdicionarUsuario/",
        params={"nome": "Remover Ponto", "email": "removerponto@example.com"}
    )
    assert response_usuario.status_code == 200
    usuario = response_usuario.json()
    usuario_id = usuario["id"]

    # Adição de um ponto geográfico para esse usuário
    response_ponto = client.post(
        "/AdicionarPonto/",
        params={
            "usuario_id": usuario_id,
            "latitude": -23.55,
            "longitude": -46.63,
            "descricao": "Ponto Removível"
        }
    )
    assert response_ponto.status_code == 200
    ponto_id = response_ponto.json()["ponto"]["id"]

    # Remoção do ponto geográfico
    response_delete = client.delete(
        "/RemoverPonto/",
        params={"ponto_id": ponto_id, "usuario_id": usuario_id}
    )
    assert response_delete.status_code == 200
    assert response_delete.json()["msg"] == "Ponto removido"

    # Verificar se ele não aparece mais na listagem
    response_listagem = client.get("/ListarPontosPorUsuario/", params={"usuario_id": usuario_id})
    assert response_listagem.status_code == 200
    assert all(p["id"] != ponto_id for p in response_listagem.json())
