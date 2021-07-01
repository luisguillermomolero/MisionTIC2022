const nombre='Maria'
const apellido='Suarez'

console.log('El nombre es: '+nombre+' '+apellido)

/*
Template Strings:Dan un formato a nuestro texto mucho mas sencillo y facil de leer. Para insertar el ` lo hacemos con: Alt + 96
Ademas, todo lo que encerremos entre ${} lo estamos evaluando como codigo de javaScript
*/

console.log(`El nombre es ${ nombre } y el apellido es ${ apellido }`)

//Hecho por Raul Esteban Benitez Enciso

//Declaración del Array con datos de usuario
const array = [
    {
        primerNombre: 'Raul',
        segundoNombre: 'Esteban',
        primerApellido: 'Benitez',
        segundoApellido: 'Enciso',
        casado: true,
        numeroTelefonoMovil: '3105706841',
        numeroTelefonoFijo:'6484110',
        ciclo: '2'
    },
    {
        primerNombre: 'Yisela',
        segundoNombre: 'Tatiana',
        primerApellido: 'Figueroa',
        segundoApellido: 'Ortiz',
        casado: false,
        numeroTelefonoMovil: '3105725555',
        numeroTelefonoFijo:'6485110',
        ciclo: '4'
    },
]

//Realizo recorrido de array a con map y obtengo el nombre del usuario con el ciclo en el cual se encuentra
array.map(element => {
    console.log (`El usuario ${element.primerNombre + ' ' + element.primerApellido} se encuentra en el ciclo ${element.ciclo}`);
})

