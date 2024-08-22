# Usar quando for CRIAR TABELAS
# from core.configs import settings

# Usar normalmente
from ..core.configs import settings

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class FilmeFavorito(settings.DBBaseModel):
    __tablename__ = 'filmes_favoritos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('usuarios.id', ondelete='CASCADE'))
    id_filme: Mapped[int] = mapped_column(ForeignKey('filmes.id', ondelete='CASCADE'))

    usuario : Mapped["Usuario"] = relationship(back_populates="filmes_favoritos", lazy="joined")
    filme : Mapped["Filme"] = relationship(back_populates="usuarios_favoritaram", lazy="joined")