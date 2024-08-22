from fastapi import FastAPI
from api.v1 import usuarios_router, filmes_router, filmes_favoritos_router
from fastapi.middleware.cors import CORSMiddleware

origins = ['*']

app = FastAPI()

app.include_router(usuarios_router, prefix="/api/v1")
app.include_router(filmes_router, prefix="/api/v1")
app.include_router(filmes_favoritos_router, prefix="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host="127.0.0.1", port=8000, log_level='info', reload=True)