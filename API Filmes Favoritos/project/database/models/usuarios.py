# Usar quando for CRIAR TABELAS
# from core.configs import settings

# Usar normalmente
from typing import List
from ..core.configs import settings

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class Usuario(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    nome: Mapped[str] = mapped_column(String(75), unique=True)
    username: Mapped[str] = mapped_column(String(35), unique=True)
    idade : Mapped[int]
    
    filmes_favoritos: Mapped[List["FilmeFavorito"]] = relationship(back_populates="usuario")

