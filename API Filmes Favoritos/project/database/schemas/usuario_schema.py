from pydantic import BaseModel as SchemaBaseModel

class UsuarioSchemaBase(SchemaBaseModel):
    nome: str
    username: str
    idade: int


class UsuarioSchemaCreate(UsuarioSchemaBase):
    pass


class UsuarioSchemaUpdate(UsuarioSchemaBase):
    pass


class UsuarioSchema(UsuarioSchemaBase):
    id: int
    
    class Config:
        orm_mode = True
    
