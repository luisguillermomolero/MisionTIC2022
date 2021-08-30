// retorna la multiplicación de 2 números
function myFunction(p1, p2) {
    return p1 * p2;   
  }


  //Convertir Fahrenheit a Celsius:
  function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
  }

  // Funciones arrow
    hello2 = () => {
        let hello;
      return "Hello World!";
    }
    // esta función puede escribirse así tambien.  Las comillas indican una cadena, así estén giradas ``
    let hello3 = () => `Hello World`;


    // funciones arrow (con un solo parámetro)
    let saludo = nombre => `Hola ${nombre}`;  //  ${nombre} indica la variable objeto nombre
       // console.log( saludo('estudiante') ); //Imprime en consola Hola estudiante

    // funciones arrow (con dos parámetros)
    let sumar = (a, b) => a + b;
      //  console.log( sumar(10, 9) ); //Imprime 19 en consola

    //producto en descuento con map y function
    let productos = ['Zapatos', 'Camisas','maletines'];
    productos = productos.map(function(producto){
        return producto + ' en descuento ';
    });
    // console.log(productos);


    //producto en descuento con arrow funtion
    let productos = ['Zapatos', 'Camisas','maletines'];
    productos = productos.map(producto => `${producto} en descuento. `);  
    // console.log(productos);


 // Función para saludar dependiendo de la hora 
  function saludar() {
    let greeting;
    let time = new Date().getHours();
    if (time < 12) {
      greeting = "Buenos dias";
    } else if (time < 18) {
      greeting = "Buenas tardes";
    } else {
      greeting = "Buenas noches";
    }
    document.getElementById("saludo").innerHTML = greeting;
  }

  
  
  // De acuerdo a la función getDay, se muestra qué día es hoy
  function hoyEsDia(){
    let dia;
    switch (new Date().getDay()) {
        case 0:
            dia = "Domingo";
            break;
        case 1:
            dia = "Lunes";
            break;
        case 2:
            dia = "Martes";
            break;
        case 3:
            dia = "Miércoles";
            break;
        case 4:
            dia = "Jueves";
            break;
        case 5:
            dia = "Viernes";
            break;
        case  6:
            dia = "Sábado";
            break;
        default:
            dia = "Dia no encontrado";
            break;
      }  
      document.getElementById("diaHoy").innerHTML = "Hoy es " + dia;
    }

    // Muestra una lista de productos con el ciclo for
    function listaProductos1(){
        let productos = ["Granos", "Verduras", "Lácteos", "Aseo", "Carnes", "Mecato"];
        let text = "";
        let x;
        for (x = 0; x < productos.length; x++) {
            text += productos[x] + "<br>";
        }
        return text;
    }
 
    // Muestra una lista de productos con el ciclo for in
    function listaProductos2(){
        let producto = {nombreProducto:"Zapatos deportivos", color:"Rojo", codigo:1525}; 
        let text = "";
        let x;
        for (x in producto) {
            text += producto[x] + " ";
        }
        return text;
    }

    // Classes en JavaScript        
    class Producto {
        constructor(nombre, codigo) {
            this.nombre = nombre;
            this.codigo = codigo;
        }
        cambiarCodigo(newCodigo){
            this.codigo = newCodigo;
        }
    }
     let producto = new Producto('Zapatos','45433');
     producto.cambiarCodigo('5433');
    // console.dir(producto);

   
   
    // Usando  alerta de estrategia para registrar
    function log(strategy){
        strategy.handle();
    }
    log(new class {
        handle(){
            alert('Usando la alerta de estrategia para registrar');
        }
    });

    //  PROMISE 
    var promise = this.$http.get('/alguna/ruta');
       
    promise.then(function(data){
             // si es exitosa hace este bloque
    }  function(err){
            // si no, hace este
    });

    // Muestra un mensaje en alert 4 segundos después de iniciar la promesa
    var timer = function(length){
        return new Promise(function(resolve, reject){
            console.log('Inicio de la promesa');
            setTimeout(function(){
                console.log('Finalizó el tiempo');

                resolve();
            }, length);
        });
    };
    timer(4000).then(() => alert('Todo terminó'));

// rest y spread
function sumar(...numeros){
    return numeros.reduce(function(prev, current){
        return prev + current;
    });
}
console.log(sumar(1,1,1,1,2,0,1,0));  // devuelve 7 

//  la función sumar escrita como arrow function
function sumar(...numeros){
    return numeros.reduce(
        (prev, current) => prev + current
    );
}

function sumar(x,y){
    return x + y;
}
let numeros = [1, 2];
console.log(sumar(...numeros));
