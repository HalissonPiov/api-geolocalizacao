from fastapi import FastAPI, HTTPException
from uuid import UUID
from .database import create_db
from .crud import *

app = FastAPI()
create_db()


@app.post("/AdicionarUsuario/")
def adicionar_usuario(nome: str, email: str):
    return criar_usuario(nome, email)

@app.put("/AtualizarUsuario/")
def atualizar_usuario(email: str, novo_nome: str):
    usuario_atualizado = editar_usuario(email, novo_nome)
    if usuario_atualizado:
        return usuario_atualizado
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.get("/ListarUsuario/")
def listar_usuario(email: str):
    usuario = buscar_usuario(email)
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/RemoverUsuario/") # Utilizar ID
def deletar_usuario(email: str):
    if remover_usuario(email):
        return {"msg": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.post("/AdicionarPonto/")
def adicionar_ponto_endpoint(usuario_id: UUID, latitude: float, longitude: float, descricao: str):
    ponto = adicionar_ponto(usuario_id=usuario_id, latitude=latitude, longitude=longitude, descricao=descricao)
    return {
        "msg": "Ponto adicionado com sucesso",
        "ponto": ponto
    }

@app.delete("/RemoverPonto/")
def deletar_ponto(ponto_id: UUID, usuario_id: UUID):
    if remover_ponto(ponto_id, usuario_id):
        return {"msg": "Ponto removido"}
    raise HTTPException(status_code=404, detail="Ponto não encontrado")

@app.put("/AtualizarPonto/")
def atualizar_ponto_endpoint(ponto_id: UUID, usuario_id: UUID, nova_latitude: float, nova_longitude: float, nova_descricao: str):
    ponto = atualizar_ponto(ponto_id, usuario_id, nova_latitude, nova_longitude, nova_descricao)
    if ponto:
        return ponto
    raise HTTPException(status_code=404, detail="Ponto não encontrado")

@app.get("/ListarPontosPorUsuario/")
def listar_pontos(usuario_id: UUID):
    return listar_pontos_usuario(usuario_id)

