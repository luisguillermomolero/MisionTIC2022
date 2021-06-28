/* Funciones: Una función es simplemente una porción de código que se va a ejecutar cuando nosotros la llamemos. Esto quiere decir que tiene que tener un nombre para poder llamarla.
Por lo tanto, le tenemos que dar un nombre y la función consta de tres partes la primera, que es el nombre.

Entre parentesis se pondran los parametros puedes recibir un parametro o varios
puede recibir un array, un objeto, un string, otras funciones
*/ 

function NombreFuncion(){
    /*Operaciones */
}

// declaracion de la funcion
function saludar(){
    console.log("Hola")
}

// Llamado a la funcion
saludar()

/* arrow function: forma sintácticamente más corta de especificar algunas funciones
    Esto lo único que hace es declarar una función 
    saludo que no recibe ningún parámetro dentro de una constante.
    No puede ser modificable   
    */

const saludo2=()=>{ console.log("Hola con const"); }
saludo2();

//Tambien se lo puede hacer con let
let saludo3=()=>{ console.log("Hola con let"); }
saludo3();

//Tambien se lo puede hacer con var
var saludo4=()=>{ console.log("Hola con var"); }
saludo4();

/*
CONST: Es una constante la cual NO cambiara su valor en ningún momento en el futuro. 
VAR: Es una variable que SI puede cambiar su valor y su scope es local. 
LET: Es una variable que también podra cambiar su valor, pero solo vivirá(Funcionara) en el bloque donde fue declarada.
*/

//Recibimos parametros que pasamos luego dentro de nuestro cuerpo y ejecutamos acciones 
//con ellos

const saludar1=(a,b,c)=> {
    console.log(a)
    console.log(b)
    console.log(c)
}
saludar1('A',123,true)

//O de esta forma
const calcular=(a,b,c)=>{
    return a+b+c//devolvemos
}
console.log(calcular(1,2,3))


//Funciones dentro de funciones 

//Devuelve un dato
const fun1=(dato)=>{
    return dato//devolvemos
}

//Imprime un dato
const fun2=(d)=>{
    console.log(d)
}
fun2(fun1("John"))