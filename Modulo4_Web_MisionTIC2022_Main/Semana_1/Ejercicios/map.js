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