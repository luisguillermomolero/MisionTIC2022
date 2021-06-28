/*Objet Destructuring: Destructuracion de objetos para no tener que acceder con el punto (.) a sus diferentes propiedades
*/

const Persona2={
    nombre:'Maria',
    apellido:'Suarez',
    edad:30,
    casado:false,
    hijo:{
        nombreHijo:'Juan'
    }
}

//Dentro de persona hay dos propiedades; "nombre" y "edad", donde cada una tiene dos valores.

//Se guarda dentro de "Persona2", estas dos propiedades instanceadas
const {nombre, edad}=Persona2

//Se imprimen las 2 propiedades
console.log(nombre)
console.log(edad)
//Se imprime la instancia de "hijo"
const {nombreHijo}=Persona2.hijo
console.log(nombreHijo)