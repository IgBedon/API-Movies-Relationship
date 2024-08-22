from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from database.core.session import get_session
from database.models.filmes_favoritos import FilmeFavorito
from database.schemas.filme_favorito_schema import *
from database.models.filmes import Filme
from database.models.usuarios import Usuario

router = APIRouter(
    prefix="/filmes_favoritos",
    tags=["filmes-favoritos"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=list[FilmeFavoritoSchema])
async def get_filmes_favoritos(db: AsyncSession = Depends(get_session)):
    filmes_favoritos = await db.execute(select(FilmeFavorito))
    return filmes_favoritos.unique().scalars().all()


@router.get('/{filme_favorito_id}', response_model=FilmeFavoritoSchema)
async def get_filme_favorito(filme_favorito_id: int, db: AsyncSession = Depends(get_session)):
    filme_favorito = await db.execute(select(FilmeFavorito).where(FilmeFavorito.id == filme_favorito_id))
    filme_favorito = filme_favorito.scalars().first()
    
    if not filme_favorito:
        raise HTTPException(status_code=404, detail="Filme Favorito not found")
    return filme_favorito


@router.post('/', response_model=FilmeFavoritoSchemaCreate)
async def create_filme_favorito(filme_favorito_data: FilmeFavoritoSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_filme_favorito = FilmeFavorito(**filme_favorito_data.model_dump())
    db.add(new_filme_favorito)
    await db.commit()
    return new_filme_favorito


@router.put('/{filme_favorito_id}', response_model=FilmeFavoritoSchema)
async def update_filme_favorito(filme_favorito_id: int, filme_favorito_data: FilmeFavoritoSchemaUpdate, db: AsyncSession = Depends(get_session)):
    stmt = (
        update(FilmeFavorito)
        .where(FilmeFavorito.id == filme_favorito_id)
        .values(**filme_favorito_data.model_dump(exclude_unset=True))  # Exclude unset values
        .returning(FilmeFavorito)
    )
    
    updated_filme_favorito = (await db.execute(stmt)).scalar_one_or_none()
    if not updated_filme_favorito:
        raise HTTPException(status_code=404, detail="Filme Favorito not found")
    
    await db.commit()
    return updated_filme_favorito


@router.delete('/{filme_favorito_id}')
async def delete_filme_favorito(filme_favorito_id: int, db: AsyncSession = Depends(get_session)):
    filme_favorito = await db.execute(select(FilmeFavorito).where(FilmeFavorito.id == filme_favorito_id))
    filme_favorito = filme_favorito.scalars().first()
    
    if not filme_favorito:
        raise HTTPException(status_code=404, detail="Filme Favorito not found")
    await db.execute(delete(FilmeFavorito).where(FilmeFavorito.id == filme_favorito_id))
    await db.commit()
    return filme_favorito