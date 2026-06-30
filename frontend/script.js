const API_URL = "http://localhost:8000";

const form = document.getElementById("formUsuario");
const tabela = document.getElementById("usuariosBody");



async function carregarUsuarios() {

    const resposta = await fetch(`${API_URL}/usuarios`);

    const usuarios = await resposta.json();

    renderizarUsuarios(usuarios);

}



function renderizarUsuarios(usuarios) {

    tabela.innerHTML = "";

    usuarios.forEach(usuario => {

        tabela.innerHTML += `
            <tr>

                <td>${usuario.id}</td>

                <td>${usuario.nome}</td>

                <td>${usuario.email}</td>

            </tr>
        `;

    });

}



async function cadastrarUsuario(event) {

    event.preventDefault();

    const usuario = {

        nome: document.getElementById("nome").value,

        email: document.getElementById("email").value,

        senha: document.getElementById("senha").value

    };

    const resposta = await fetch(`${API_URL}/usuarios`, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(usuario)

    });

    if (!resposta.ok) {

        alert("Erro ao cadastrar usuário.");

        return;

    }

    form.reset();

    carregarUsuarios();

}



form.addEventListener("submit", cadastrarUsuario);

carregarUsuarios();