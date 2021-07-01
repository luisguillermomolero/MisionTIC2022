/*Objet Destructuring: Destructuracion de objetos para no tener que acceder con el punto (.) a sus diferentes propiedades
*/

const Persona2 = {
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
const { nombre, edad } = Persona2

//Se imprimen las 2 propiedades
console.log(nombre)
console.log(edad)
//Se imprime la instancia de "hijo"
const { nombreHijo } = Persona2.hijo
console.log(nombreHijo)

//Hecho por Raul Esteban Benitez Enciso

//Declaración de objeto con datos del usuario
const objeto = {
    primerNombre: 'Raul',
    segundoNombre: 'Esteban',
    primerApellido: 'Benitez',
    segundoApellido: 'Enciso',
    casado: true,
    numeroTelefonoMovil: '3105706841',
    numeroTelefonoFijo:'6484110',
    residencia: {
        pais: 'Colombia',
        departamento: 'Meta',
        ciudad: 'San Juan de Arama',
    },
    direccion: {
        calle:'17',
        carrera: '15',
        numero: '18'
    }
}

//Realizo la destructuración
const {residencia, primerNombre, primerApellido} = objeto;

//Imprimo en pantalla el nombre del usuario y su lugar de residencia
console.log(`El señor ${primerNombre + ' ' + primerApellido} vive en ${residencia.ciudad + ', ' + residencia.departamento + ' - ' + residencia.pais}`);

//Ejercicio Destructuring - Realizado por: Brandon Motta - Grupo Web 4A

//Objeto teléfono
const telefono = {
    marca: "Xiaomi",
    modelo: "Redmi Note 7",
    color: "Negro",
    releaseYear: 2019,
    accesorios: {
        vidrioTemplado: true,
        fundaProtectora: true,
    },
    funciona: true
}

//Guardo el modelo, el año de salida (releaseYear) y el color  dentro de "telefono"
const { modelo, releaseYear, color} = telefono

//Imprimo estas propiedades
console.log(`Modelo: ${ modelo }`)
console.log(`Año de Salida: ${ releaseYear }`)
console.log(`Color: ${ color }`)

//Separo la instancia de los accesorios
const { fundaProtectora, vidrioTemplado } = telefono.accesorios

//Finalmente las imprimo
console.log(`Vidrio Templado: ${ vidrioTemplado }`)
console.log(`Funda Protectora: ${ fundaProtectora }`)

//Juan Esteban Uran Sierra. Grupo 4A

//Diccionario con los datos de las personas
const persona={
    nombre:'juan esteban',
    apellido:'uran sierra',
    edad:21,
    hijo:{
        nombreHijo:'pedro'
    },
    hermano:{
        nombreHermano:'valeria',
        edad:25,
        hijoHermano:{
        nombreHijoHermano: 'luis',
        edad: 5
        }
    },
    telefono:'3215821937',
    ocupacion:'desarrollador',
    casado:true,
    sueldo:15000000,
    experiencia:5,
    lenguajeQueManeja:{
        nombreLenguaje:'java'
    }
}

const { nombre, apellido, edad, telefono, ocupacion, casado } = persona //destructuracion del array 
const { nombreHermano } = persona.hermano //destructuracion del array 
const { nombreHijoHermano } = persona.hermano.hijoHermano //destructuracion del array 

console.log(nombre, apellido) //imprimir variables
console.log(nombreHermano)  //imprimir variables
console.log(nombreHijoHermano) //imprimir variables

