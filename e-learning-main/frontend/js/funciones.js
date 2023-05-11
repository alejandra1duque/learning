// Primero vamos a crear un metodo

/*  Cuando el todo el documento este cargado me va a ejecutar una funcion
    eso es lo que significa DOMContentLoaded, y me carga la funcion init

 */
document.addEventListener("DOMContentLoaded", init);

//voy a generar una variable para agregar la API generada en mi backend
// lo dejare hasta api, si deseo consultar usuarios, concateno usuarios si voya consultar cliente concateno cliente.

const URL_API = "http://127.0.0.1:3000/api/";

// como vasicamente voy a tener todos los usuarios voy a crear una variable que va a tener un array.

let users = [];

//creamos la funcion init
//En esta funcion va a cargar los usuarios del sistema, la idea es que cuando cargue el documento, este documento haga la peticion al servidor para que esta peticion  le devuelva los datos .

function init() {
  // * Ver Usuarios
  verUsuarios();
}

// * FUNCION VER USUARIOS **************************************************

async function verUsuarios() {
  // * --> Creamos una variable llamada url y concatenamos users con la constante URL_APÍ
  // * --> con esta concatenacion podemos ver todos los usuarios.
  let url = URL_API + "users";

  // * --> Hacemos la peticion
  // * --> hacemos una peticion fetch para traer la informacion.
  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "aplication/json",
      // * --> con el headers decimos que tipo de estructura es.
    },
  });
  // * --> con esto me trae los datos pero hay que generar la estructura JSON completa.
  // *--> ya teniendo el response, creamos una variable llamada users.
  users = await response.json(); // *--> toma la respuesta para consultar los usuarios en formato json.
  console.log(users);
}
