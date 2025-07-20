import pytest
from httpx import AsyncClient
from uuid import UUID
from app.main import app

@pytest.mark.asyncio
async def test_criar_usuario():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/AdicionarUsuario/", params={"nome": "Teste", "email": "teste@exemplo.com"})
        assert response.status_code == 200
        assert "id" in response.json()

@pytest.mark.asyncio
async def test_adicionar_e_listar_ponto():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_resp = await ac.post("/AdicionarUsuario/", params={"nome": "Geo", "email": "geo@ex.com"})
        user_id = user_resp.json()["id"]

        ponto_resp = await ac.post("/AdicionarPonto/", params={
            "usuario_id": user_id,
            "latitude": -23.5,
            "longitude": -46.6,
            "descricao": "Escola"
        })
        assert ponto_resp.status_code == 200
        assert ponto_resp.json()["descricao"] == "Escola"

        listar_resp = await ac.get("/ListarPontosPorUsuario/", params={"usuario_id": user_id})
        assert listar_resp.status_code == 200
        assert len(listar_resp.json()) >= 1

@pytest.mark.asyncio
async def test_remover_usuario():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post("/AdicionarUsuario/", params={"nome": "Delete", "email": "delete@ex.com"})
        response = await ac.delete("/RemoverUsuario/", params={"email": "delete@ex.com"})
        assert response.status_code == 200
        assert response.json()["msg"] == "Usuário removido"
