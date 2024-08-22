from pydantic import BaseModel as SchemaBaseModel
from .filme_schema import FilmeSchema
from .usuario_schema import UsuarioSchema

class FilmeFavoritoSchemaBase(SchemaBaseModel):
    id_usuario: int
    id_filme: int


class FilmeFavoritoSchemaCreate(FilmeFavoritoSchemaBase):
    pass


class FilmeFavoritoSchemaUpdate(FilmeFavoritoSchemaBase):
    pass


class FilmeFavoritoSchema(SchemaBaseModel):
    usuario: UsuarioSchema
    filme: FilmeSchema
 
    class Config:
        orm_mode = True   
    
