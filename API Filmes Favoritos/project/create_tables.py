from database.core.configs import settings
from database.core.engine import engine


async def create_tables() -> None:
    from database.models import filmes, usuarios, filmes_favoritos
    
    print("Criando Tabelas")
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabelas criadas com sucesso")


if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())