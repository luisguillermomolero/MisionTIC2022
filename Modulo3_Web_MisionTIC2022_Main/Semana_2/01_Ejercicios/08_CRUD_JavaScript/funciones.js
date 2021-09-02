var dbClientes = localStorage.getItem("dbClientes"); //Obtener datos de localStorage
var operacion = "A"; //"A"=agregar; "E"=editar
dbClientes = JSON.parse(dbClientes); // Covertir a objeto
if (dbClientes === null)
  // Si no existe, creamos un array vacio.
  dbClientes = [];

function Mensaje(t) {
  switch (t) {
    case 1: //
      $(".mensaje-alerta").append(
        "<div class='alert alert-success' role='alert'>Se agrego con exito!</div>"
      );
      break;
    case 2: //
      $(".mensaje-alerta").append(
        "<div class='alert alert-danger' role='alert'>Se elimino el cliente</div>"
      );
      break;
    default:
  }
}

function AgregarCliente() {
  // Seleccionamos los datos de los inputs de formulario
  var datos_cliente = JSON.stringify({
    Nombre: $("#nombre").val(),
    Correo: $("#correo").val(),
    Fecha_nacimiento: $("#fecha_nacimiento").val(),
  });

  dbClientes.push(datos_cliente); // Guardar datos en el array definido globalmente
  localStorage.setItem("dbClientes", JSON.stringify(dbClientes));

  ListarCliente();

  return Mensaje(1);
}

function ListarCliente() {
  $("#dbClientes-list").html(
    "<thead>" +
      "<tr>" +
      "<th> ID </th>" +
      "<th> Nombre </th>" +
      "<th> Correo </th>" +
      "<th> fecha_nacimiento </th>" +
      "<th> </th>" +
      "<th>  </th>" +
      "</tr>" +
      "</thead>" +
      "<tbody>" +
      "</tbody>"
  );

  for (var i in dbClientes) {
    var d = JSON.parse(dbClientes[i]);
    $("#dbClientes-list").append(
      "<tr>" +
        "<td>" +
        i +
        "</td>" +
        "<td>" +
        d.Nombre +
        "</td>" +
        "<td>" +
        d.Correo +
        "</td>" +
        "<td>" +
        d.Fecha_nacimiento +
        "</td>" +
        "<td> <a id='" +
        i +
        "' class='btnEditar' href='#'> <span class='glyphicon glyphicon-pencil'> </span>  </a> </td>" +
        "<td> <a id='" +
        i +
        "' class='btnEliminar' href='#'> <span class='glyphicon glyphicon-trash'> </span> </a> </td>" +
        "</tr>"
    );
  }
}

if (dbClientes.length !== 0) {
  ListarCliente();
} else {
  $("#dbClientes-list").append("<h2> No tienes clientes </h2>");
}

function contarCliente() {
  var cliente = dbClientes;
  nCliente = cliente.length;

  $("#numeroClientes").append(
    "<a>Tienes actualmente" +
      "<br>" +
      "<span class='badge'>" +
      nCliente +
      "</span></a> Clientes"
  );
  return nCliente;
}

function Eliminar(e) {
  dbClientes.splice(e, 1); // Args (posición en el array, numero de items a eliminar)
  localStorage.setItem("dbClientes", JSON.stringify(dbClientes));
  return Mensaje(2);
}

function Editar() {
  dbClientes[indice_selecionado] = JSON.stringify({
    Nombre: $("#nombre").val(),
    Correo: $("#correo").val(),
    Fecha_nacimiento: $("#fecha_nacimiento").val(),
  });
  localStorage.setItem("dbClientes", JSON.stringify(dbClientes));// agregar al almacen
  operacion = "A"; //Regresamos la valor original
  return true;
}

$(".btnEliminar").bind("click", function () {
  alert("¿ Me quieres eliminar ?");
  indice_selecionado = $(this).attr("id"); // "this" contiene el elemento clikeado en el contexto actual
  console.log(indice_selecionado);
  console.log(this);
  Eliminar(indice_selecionado); // Eliminamos el elemento llamando la funcion de eliminar
  ListarCliente();
});

$(".btnEditar").bind("click", function () {
  alert("¿ Me quieres editar ?");
  // Cambiamos el modo
  $(".modo").html(
    "<span class='glyphicon glyphicon-pencil'> </span> Modo edición"
  );
  operacion = "E";
  indice_selecionado = $(this).attr("id");
  console.log(indice_selecionado);
  console.log(this);
  // Llemanos el formulario con los datos actuales del cliente a editar
  var clienteItem = JSON.parse(dbClientes[indice_selecionado]);
  $("#nombre").val(clienteItem.Nombre);
  $("#correo").val(clienteItem.Correo);
  $("#fecha_nacimiento").val(clienteItem.Fecha_nacimiento);
  $("#nombre").focus();
});

contarCliente();
// Esperar el evento de envio del formulario !!
$("#cliente-form").bind("submit", function () {
  debugger;
  if (operacion == "A") return AgregarCliente();
  else {
    return Editar();
  }
});
