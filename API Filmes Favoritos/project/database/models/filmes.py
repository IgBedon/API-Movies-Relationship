# Usar quando for CRIAR TABELAS
# from core.configs import settings

# Usar normalmente
from typing import List
from ..core.configs import settings

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class Filme(settings.DBBaseModel):
    __tablename__ = 'filmes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    titulo: Mapped[str] = mapped_column(String(75), unique=True)
    descricao : Mapped[str]
    img: Mapped[str]

    usuarios_favoritaram: Mapped[List["FilmeFavorito"]] = relationship(back_populates="filme")