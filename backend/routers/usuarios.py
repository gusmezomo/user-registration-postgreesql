from fastapi import APIRouter

from schemas.usuario import UsuarioCreate, UsuarioResponse
from services.usuario_service import (
    criar_usuario,
    listar_usuarios,
)

router = APIRouter()


@router.get(
    "/usuarios",
    response_model=list[UsuarioResponse]
)
def buscar_usuarios():

    return listar_usuarios()


@router.post("/usuarios", status_code=201)
def cadastrar_usuario(usuario: UsuarioCreate):

    criar_usuario(usuario)

    return {
        "mensagem": "Usuário cadastrado com sucesso!"
    }