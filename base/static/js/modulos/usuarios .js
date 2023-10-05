document.addEventListener("DOMContentLoaded", function () {

    var tipoUsuario = document.getElementById("id_tipo_usuario");
    var camposAdministrador = document.getElementById("campos_administrador");
    var camposMecanico = document.getElementById("campos_mecanico");
    var camposSecretaria = document.getElementById("campos_Secretaria");
    var camposCliente = document.getElementById("campos_cliente");

    tipoUsuario.addEventListener("change", function () {

        camposAdministrador.style.display = "none";
        camposMecanico.style.display = "none";
        camposSecretaria.style.display = "none";
        camposCliente.style.display = "none";


        if (tipoUsuario.value === "Administrador") {
            camposAdministrador.style.display = "block";
        } else if (tipoUsuario.value === "Mecanico") {
            camposMecanico.style.display = "block";
        } else if (tipoUsuario.value === "Secretaria") {
            camposSecretaria.style.display = "block";
        } else if (tipoUsuario.value === "Cliente") {
            camposCliente.style.display = "block";
        }
    });

  
    tipoUsuario.dispatchEvent(new Event("change"));
});