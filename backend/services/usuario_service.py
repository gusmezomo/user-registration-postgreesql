from database import get_connection


def listar_usuarios():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT
                    id,
                    nome,
                    email,
                    ativo,
                    criado_em
                FROM usuarios
                ORDER BY id
            """)

            usuarios = cur.fetchall()

    return [
        {
            "id": usuario[0],
            "nome": usuario[1],
            "email": usuario[2],
            "ativo": usuario[3],
            "criado_em": usuario[4],
        }
        for usuario in usuarios
    ]


def criar_usuario(usuario):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO usuarios
                    (nome, email, senha)
                VALUES
                    (%s, %s, %s)
                """,
                (
                    usuario.nome,
                    usuario.email,
                    usuario.senha,
                ),
            )

        conn.commit()