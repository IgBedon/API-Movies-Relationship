from pydantic import BaseModel as SchemaBaseModel

class FilmeSchemaBase(SchemaBaseModel):
    titulo: str
    descricao: str
    img: str


class FilmeSchemaCreate(FilmeSchemaBase):
    pass


class FilmeSchemaUpdate(FilmeSchemaBase):
    pass


class FilmeSchema(FilmeSchemaBase):
    id: int

    class Config:
        orm_mode = True
    
    
