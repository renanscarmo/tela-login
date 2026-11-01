const formulario = document.querySelector("form");
const campoUsuario = document.getElementById("usuario");
const campoSenha = document.getElementById("senha");
const mensagem = document.getElementById("mensagem");
formulario.addEventListener("submit" , function (evento) {
    evento.preventDefault();
    mensagem.textContent = "Você Clicou em entrar";

});
