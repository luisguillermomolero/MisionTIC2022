/*Javascript asincrono: Cuando se esta trabajando con "promesas" con el metodo ".then" nuestro programa esta trabajando dentro de un "proceso" o "hilo", ejecutando el código de arriba hacia abajo secuencialmente, esto quiere decir, que se ejecuta una instruccion seguida de la otra. 

Nuestro programa es como un hilo que va cayendo, en cuanto se encuetre a una promesa genera un hilo aparte que baja exactamente igual a la vez que el hilo principal "sin detener el hilo principal". Si no se trabaja con promesas mientras se esta esperando que ".then" nos devuelva una respuesta, nuestro hilo principal se detendria, el programa se detiene y cuando nos devuelve un verdadero el codigo se sigue ejecutando. 

Con el uso de las promesas, evitamos que se detenga nuestro programa, ya que nuestro hilo principal se ejecuta y de forma paralela, se crea un hilo secundario donde se ejecuta la promesa; una vez se ejecute esta promesa, volvera al hilo principal. 
*/


// fetch('http://jsonplaceholder.typicode.com/todos/1')

//     .then( response =>response.json())
//     .then( json => console.log (json.userId))
//     .catch( e => console.log(e))

/*
En el siguiente ejemplo, se muestra una funcion asincrona. Cuando se llega a este codigo, se informa que se va a crear un hilo secundario que inicia en paralelo con respecto al hilo principal, sin embargo, el hilo principal no se detiene.
*/

const obtenerUsuario = async() =>{//No recibe ningun parametro en este caso
    //Para capturar errores vamos a trabajar con el metodo try y catch
    try{
        /* En este bloque se coloca todo lo que se va a ejecutar
        
        await : espera 
        
        Esperar que fetch devuelva una respuesta y la guarda dentro de una constante que se llama respuesta */

        const respuesta = await fetch('http://jsonplaceholder.typicode.com/todos/1')

        //La respuesta la llevamos a un json y esta se va a encontrar en datos

        const datos = await respuesta.json()
        console.log(datos)
        
    }catch(e){
        //Aqui van los errores es decir que si en algun momento en try se produce un error
        //automaticamente se ejecuta lo que esta el el catch
        console.log(e)
    }

}

obtenerUsuario()