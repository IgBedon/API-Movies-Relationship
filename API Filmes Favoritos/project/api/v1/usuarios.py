from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from database.core.session import get_session
from database.models.usuarios import Usuario
from database.schemas.usuario_schema import *

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    dependencies="",
    responses="",
)


@router.get('/', response_model=list[UsuarioSchema])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    usuarios = await db.execute(select(Usuario))
    return usuarios.scalars().all()


@router.get('/{usuario_id}', response_model=UsuarioSchema)
async def get_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    usuario = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
    usuario = usuario.scalars().first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return usuario


@router.post('/', response_model=UsuarioSchema)
async def post_usuario(usuario_data: UsuarioSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_usuario = Usuario(**usuario_data.model_dump())
    db.add(new_usuario)
    await db.commit()
    return new_usuario


@router.put('/{usuario_id}', response_model=UsuarioSchema)
async def put_usuario(usuario_id: int, usuario_data: UsuarioSchemaUpdate, db: AsyncSession = Depends(get_session)):
    stmt = (
        update(Usuario)
        .where(Usuario.id == usuario_id)
        .values(**usuario_data.model_dump(exclude_unset=True))  # Exclua valores não definidos
        .returning(Usuario)
    )
    
    updated_usuario = (await db.execute(stmt)).scalar_one_or_none()
    if not updated_usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    
    await db.commit()
    return updated_usuario


@router.delete('/{usuario_id}')
async def delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    usuario = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
    usuario = usuario.scalars().first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    await db.execute(delete(Usuario).where(Usuario.id == usuario_id))
    await db.commit()
    return usuario