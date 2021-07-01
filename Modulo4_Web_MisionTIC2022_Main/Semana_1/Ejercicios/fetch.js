/*
Fetch es una funcion que nos permite trabajar a traves de promesas (es un objeto que representa la terminación o el fracaso de una operación asíncrona) para hacer peticiones a las APIs (interfaz de programación de aplicaciones) donde se puede extraer el codigo y mostrarlo.

Se lo puede correr en cualquier navegador ya que todos trabajan con motor v8 de javaScript, asimismo, todas las API's, cuentan con ellas en su core
*/

// Recibe como unico parametro la url donde va hacer la peticion.

fetch('http://jsonplaceholder.typicode.com/todos/1')//devuelve un objeto json

//fetch trabaja con promesas
//then Inicia la promesa y lo que trae en fetch viaja en la respuesta (response)

    .then( response =>response.json())//A traves de la flecha se transforma esta respuesta en un objeto json

    //Se convierte en un objeto json para manipularlo mas facilmente
    //A continuacion se llama a otra promesa y captura el objeto para imprimirlo
    .then( json => console.log( json))
    
    //Solo debe haber un then
    //.then( json => console.log (json.userId))

    //los errores se capturan con catch y en este caso lo imprime
    .catch( e => console.log(e))

    /*
    Las promesas solo dan true cuando son positivas es decir si fetch da positivo
    pasara a la promesa si la promesa da positivo
    pasara a la siguiente promesa
    Si en alguno de los momentos esto falla se pasa directamente al catch
    */


//const name = 'Simplilearn';
//const greet = <h1>Hello, {name}</h1>;
