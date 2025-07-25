from .models import Usuario, PontoGeografico
from .database import get_session
from sqlmodel import select
from typing import List
from uuid import UUID

def criar_usuario(nome: str, email: str):
    with get_session() as session:
        usuario = Usuario(nome=nome, email=email)
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario

def remover_usuario(email: str):
    with get_session() as session:
        usuario = session.exec(select(Usuario).where(Usuario.email == email)).first()
        if usuario:
            session.delete(usuario)
            session.commit()
            return True
        return False

def editar_usuario(email: str, novo_nome: str):
    with get_session() as session:
        usuario = session.exec(select(Usuario).where(Usuario.email == email)).first()
        if usuario:
            usuario.nome = novo_nome
            session.add(usuario)
            session.commit()
            session.refresh(usuario)
            return usuario
        return None

def buscar_usuario(email: str):
    with get_session() as session:
        return session.exec(select(Usuario).where(Usuario.email == email)).first()

def adicionar_ponto(usuario_id: UUID, latitude: float, longitude: float, descricao: str):
    with get_session() as session:
        ponto = PontoGeografico(latitude=latitude, longitude=longitude, descricao=descricao, usuario_id=usuario_id)
        session.add(ponto)
        session.commit()
        session.refresh(ponto)
        return ponto

def remover_ponto(ponto_id: UUID, usuario_id: UUID):
    with get_session() as session:
        ponto = session.exec(
            select(PontoGeografico).where(PontoGeografico.id == ponto_id, PontoGeografico.usuario_id == usuario_id)
        ).first()
        if ponto:
            session.delete(ponto)
            session.commit()
            return True
        return False

def atualizar_ponto(ponto_id: UUID, usuario_id: UUID, nova_latitude: float, nova_longitude: float, nova_descricao: str):
    with get_session() as session:
        ponto = session.exec(
            select(PontoGeografico).where(PontoGeografico.id == ponto_id, PontoGeografico.usuario_id == usuario_id)
        ).first()
        if ponto:
            ponto.latitude = nova_latitude
            ponto.longitude = nova_longitude
            ponto.descricao = nova_descricao
            session.add(ponto)
            session.commit()
            session.refresh(ponto)
            return ponto
        return None


def listar_pontos_usuario(usuario_id: UUID) -> List[PontoGeografico]:
    with get_session() as session:
        pontos = session.exec(select(PontoGeografico).where(PontoGeografico.usuario_id == usuario_id)).all()
        return pontos