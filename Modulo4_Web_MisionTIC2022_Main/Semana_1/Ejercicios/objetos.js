//Objetos: constantes o variables declaradas 
//que tienes diferentes propiedades con diferentes valores(texto, numerico,booleanos, objeto)

//Definicion de un objeto igual que una variable 
//El objeto puede tener varias propiedades y valores
const Persona={
    nombre:'Maria',
    apellido:'Suarez',
    edad:30,
    casado:false
}

//Acceder a las propiedades
console.log(Persona)

//Se pueden acceder a estas propiedades con el punto
console.log(Persona.nombre)
console.log(Persona.apellido)
console.log(Persona.edad)
console.log(Persona.casado)

//  Podemos agregar propiedades al objeto
Persona.id = 1
console.log(Persona)

//Objeto que tiene como valor un objeto
const Persona2={
    nombre:'Maria',
    apellido:'Suarez',
    edad:30,
    casado:false,
    hijo:{nombreHijo:'Juan'}
}

//Realizado por: Julian David Montero. Grupo Web 4A-4
console.log(Persona2.hijo.nombreHijo)

const carro = {
    marca: 'BMW',
    color: 'Negro',
    propietario: {
      nombre: 'Julian', apellido: 'Montero'
    },
    modelo: '2019',
    llantas: 4,
    pasajeros: [1, 2, 3, 4],
    motor: '4 caballos',
    'primeros auxilios': true,
    luz: {
      delantera: true,
      trasera: true
    },
    seguro: {
      nombre: 'SURA',
      vigente: 2025
    },
    licencia: {
      expedicion: 2021,
      vigente: 2025
    }
  }
  
  console.log(carro.propietario.nombre)
  console.log(carro.seguro.vigente)
  console.log(carro.luz.trasera)
  console.log(carro.licencia)
  
//Leidy Johanna Castañeda. Grupo 4A-4

const persona={
    nombre:'juan esteban',
    apellido:'uran sierra',
    edad:21,
    hijo:{
        nombreHijo:'pedro'
    },
    hermano:{
        nombreHermano:'valeria',
        edad:25
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
console.log(persona.nombre)
console.log(persona.hijo.nombreHijo)
console.log(persona.lenguajeQueManeja.nombreLenguaje)

