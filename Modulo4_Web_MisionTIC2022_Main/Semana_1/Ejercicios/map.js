//Recorrer este array
const datos=[
    {nombre:'Ivan', edad:37},
    {nombre:'Maria',edad:50},
    {nombre:'Rosa', edad:20},
    {nombre:'Luis',edad:22}
]

//Recorrido con forEach
datos.forEach(elemento=> {
    console.log(elemento)
    console.log(elemento.nombre)
    console.log(elemento.edad)
})

//Recorrido con map; mas rapido que forEach
datos.map(elemento=> {
    console.log(elemento)
    console.log(elemento.nombre)
    console.log(elemento.edad)
})

//Ejercicio Map - Realizado por: Brandon Motta - Grupo Web 4A - 4

//Array a recorrer
const objetos = [
    {nombre: 'Caja', color: 'Negro'}, //Objetos de distinto color
    {nombre: 'Vaso', color: 'Rojo'},
    {nombre: 'Jarro', color: 'Azul'},
    {nombre: 'Tazón', color: 'Rosa'}
]

//Recorrido con ForEach
objetos.forEach(elemento=> {
    console.log(elemento)           //Retorna el Objeto completo
    console.log(elemento.nombre)    //Retorna el nombre del Objeto
    console.log(elemento.color)     //Retorna el color del Objeto
})

//Recorrido con Map
objetos.map(elemento=> {
    console.log(elemento)           //Retorna el Objeto completo
    console.log(elemento.nombre)    //Retorna el nombre del Objeto
    console.log(elemento.color)     //Retorna el color del Objeto
})

//Juan Esteban Uran Sierra. Grupo 4A-4

//Array con los datos de las personas
const datosPersonas = [
    {nombre:'luis', edad:10},
    {nombre:'pedro', edad:20},
    {nombre:'maria', edad:30}
]

//recorrido del array datosPersonas con un forEach
datosPersonas.forEach(element => {
    console.log(element) //imprime el valor del objeto
    console.log(element.nombre) //imprime el nombre del objero 
    console.log(element.edad) //imprime edad del objeto
});

//recorrido del array datosPersonas con un map
datosPersonas.map(element => {
    console.log(element) //imprime el valor del objeto
    console.log(element.nombre) //imprime el nombre del objero 
    console.log(element.edad) //imprime edad del objeto
});

//Hecho por Raul Esteban Benitez Enciso. Grupo 4A-4
//objeto
const objeto = [
    {
        primerNombre: 'Raul',
        segundoNombre: 'Esteban',
        primerApellido: 'Benitez',
        segundoApellido: 'Enciso',
        casado: true,
        numeroTelefonoMovil: '3105706841',
        numeroTelefonoFijo:'6484110',
    },
    {
        primerNombre: 'Yisela',
        segundoNombre: 'Tatiana',
        primerApellido: 'Figueroa',
        segundoApellido: 'Ortiz',
        casado: false,
        numeroTelefonoMovil: '3105725555',
        numeroTelefonoFijo:'6485110',
    },
]

//recorrer array con forEach, muestra elemento completo y luego primer nombre
objeto.forEach(element => {
    console.log(element);
   console.log(element.primerNombre);
})

//Recorrer array con map, muestra elemento completo y luego si está casado
objeto.map(element=>{
    console.log(element);
    console.log(element.casado);
})
