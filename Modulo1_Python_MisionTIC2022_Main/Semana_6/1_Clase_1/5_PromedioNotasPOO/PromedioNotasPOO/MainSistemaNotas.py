##################
#Aplicación de notas 
#(Intermediación con el mundo del problema)
##################

#Importar las clases que representan las entidades del mundo del problema
from Nota import Nota
from Materia import Materia

#Sección principal de la aplicación
###################################

#Instanciar: crear los objetos tipo nota
objetoNota1 = Nota(nota100=40,descripcion='Primer Parcial')
objetoNota2 = Nota(nota100=50,descripcion='Segundo Parcial')
objetoNota3 = Nota(nota100=39,descripcion='Tercer Parcial')
objetoNota4 = Nota(nota100=76,descripcion='Cuarto Parcial')
objetoNota5 = Nota(nota100=96,descripcion='Quinto Parcial')

#Ilustración de uso y actualización de la clase, objeto y atributos
# print('Nota 1 en escala cualitativa:',objetoNota1.notaCualitativa)
# print('Nota 1 en escala cualitativa:',objetoNota1.getNotaCualitativa())
# print('Fecha de registro Nota 1',objetoNota1.getFechaRegistro())
# print('Nota 1 en escala de 5',objetoNota1.getNota5())
# objetoNota4.descripcion = 'Nueva descripción'
# objetoNota4.setDescripcion('Nueva descripción')
# print(objetoNota4)

#Pedir al objeto que se muestre en pantalla (consola)
print("***Notas")
objetoNota1.mostrarInfoNota()
objetoNota2.mostrarInfoNota()
objetoNota3.mostrarInfoNota()
objetoNota4.mostrarInfoNota()
objetoNota5.mostrarInfoNota()

#Instanciar: crear los objetos tipo nota
objetoMateria = Materia(nota1=objetoNota1, nota2=objetoNota2, nota3=objetoNota3, nota4=objetoNota4, nota5=objetoNota5,nombre="Estructura de Lenguajes", creditos=3)

#Realizar varias versiones de promedio para la materia
objetoMateria.calcularPromedio5()
objetoMateria.calcularPromedio100()
objetoMateria.calcularPromedioAjustado5()
objetoMateria.calcularPromedioAjustado100()

#Solicitar a la materia que se muestre en pantalla
print("***Materia (Respuesta al requerimiento)")
objetoMateria.mostrarInfoMateria()

#Ilustración de funcionalidad dinámica adicionada: atributo tipo lista para que la materia pueda contener más notas
# objetoMateria.adicionarNota( Nota(nota100=100,descripcion='Adicional') )
# print('Última adicionada')
# objetoMateria.mostrarUltimaNota()