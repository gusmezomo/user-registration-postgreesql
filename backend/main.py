from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.usuarios import router as usuarios_router

app = FastAPI(title="Learning PostgreSQL")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router)