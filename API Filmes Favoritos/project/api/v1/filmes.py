from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from database.core.session import get_session
from database.models.filmes import Filme
from database.schemas.filme_schema import *

router = APIRouter(
    prefix="/filmes",
    tags=["filmes"],
    dependencies="",
    responses="",
)


@router.get('/', response_model=list[FilmeSchema])
async def get_filmes(db: AsyncSession = Depends(get_session)):
    filmes = await db.execute(select(Filme))
    return filmes.scalars().all()


@router.get('/{filme_id}', response_model=FilmeSchema )
async def get_filme(filme_id: int, db: AsyncSession = Depends(get_session)):
    filme = await db.execute(select(Filme).where(Filme.id == filme_id))
    filme = filme.scalars().first()
    
    if not filme:
        raise HTTPException(status_code=404, detail="Filme not found")
    return filme


@router.post('/', response_model=FilmeSchema)
async def post_filme(filme_data: FilmeSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_filme = Filme(**filme_data.model_dump())
    db.add(new_filme)
    await db.commit()
    return new_filme


@router.put('/{filme_id}', response_model=FilmeSchema)
async def put_filme(filme_id: int, filme_data: FilmeSchemaUpdate, db: AsyncSession = Depends(get_session)):
    stmt = (
        update(Filme)
        .where(Filme.id == filme_id)
        .values(**filme_data.model_dump(exclude_unset=True))  # Exclua valores não definidos
        .returning(Filme)
    )
    
    updated_filme = (await db.execute(stmt)).scalar_one_or_none()
    if not updated_filme:
        raise HTTPException(status_code=404, detail="Filme not found")
    
    await db.commit()
    return updated_filme


@router.delete('/{filme_id}')
async def delete_filme(filme_id: int, db: AsyncSession = Depends(get_session)):
    filme = await db.execute(select(Filme).where(Filme.id == filme_id))
    filme = filme.scalars().first()
    
    if not filme:
        raise HTTPException(status_code=404, detail="Filme not found")
    await db.execute(delete(Filme).where(Filme.id == filme_id))
    await db.commit()
    return filme