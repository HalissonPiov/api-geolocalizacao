from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import uuid4, UUID

class Usuario(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True) #
    nome: str
    email: str = Field(index=True, unique=True)
    pontos: List["PontoGeografico"] = Relationship(back_populates="usuario") #

class PontoGeografico(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    latitude: float
    longitude: float
    descricao: str
    usuario_id: UUID = Field(foreign_key="usuario.id")
    usuario: Optional[Usuario] = Relationship(back_populates="pontos")