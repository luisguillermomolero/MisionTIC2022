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
const fun2=(d)=>{ console.log(d) }
fun2(fun1("John"))

//Juan Esteban Uran Sierra. Grupo 4A-4
const func2=(valor)=>{
    console.log(valor/3) 
}

const func1=(num1,num2,num3)=>{
    return num1+num2+num3
}
func2(func1(4,5,6))

let multiplicar=(num1,num2,num3) =>{
    console.log(num1+num2*num3)
}
multiplicar(1,2,3)

//Relizado por: Julian David Montero Gonzalez. Grupo 4A-4
const sumar = (num1, num2) => {
    if (num1 > 0 && num2 > 0) {
        return Math.pow(num1, num2)
    }
    return `${num1} y ${num2} tienen que ser mayores`
}
const imprimir = res => {
if (isNaN(res)) {
    console.log(`${res} :(`)
} else {
    console.log(`El valor es ${res}`)
}
}

imprimir(sumar(1, 7))

//Ejercicio Funciones     Realizado por: Brandon Motta       Grupo Web 4

function funcion1(c){
    console.log("La cantidad de letras de la palabra ingresada es: " + c)
}

function cantLetras(palabra) {
    let cantLetras = palabra.length;
    return (cantLetras);
}
funcion1(cantLetras("Patata"));

//Funciones (Jhon Sanabria)
//Funcion Nombre con dos parametros de entrada
const functName=(nombre,edad)=>{
    return nombre,edad
}
// Funcion Edad 
const functEdad=(fActual,fnacido)=>{
    return fActual - fnacido
}
//llamadoa la funcion edad desde la funcion nombre
console.log(functName('Felipe',functEdad(2021,2002)))

// calculo IMC  Ruben Rodriguez. Grupo 4A-4
const imc=(pesoKg, estaturaCm)=>{
    return pesoKg/estaturaCm
}

const mostrar=(p)=>{
    console.log(p)
}

mostrar(imc(80,182))
