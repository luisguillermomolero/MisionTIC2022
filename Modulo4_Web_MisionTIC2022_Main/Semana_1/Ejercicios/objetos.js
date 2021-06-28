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

Persona.id=1
console.log(Persona)

//Objeto que tiene como valor un objeto

const Persona2={
    nombre:'Maria',
    apellido:'Suarez',
    edad:30,
    casado:false,
    hijo:{
        nombreHijo:'Juan'

    }
}


//Para acceder a Juan seria

console.log(Persona2.hijo.nombreHijo)


