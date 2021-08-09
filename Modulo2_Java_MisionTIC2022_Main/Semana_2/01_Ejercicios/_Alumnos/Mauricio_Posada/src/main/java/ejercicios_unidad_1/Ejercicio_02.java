package ejercicios_unidad_1;

import java.util.Scanner;

// Elaborado por Mauricio Posada Grupo P72
/*
2. Realizar un programa que realice el promedio de las notas de un alumno, para ello el programa va a tener
que solicitar el nombre del alumno y las notas de las 3 evaluaciones. Si el alumno tiene un promedio mayor o 
igual a 3.0 también debe imprimir “Aprobado”, si no alcanzó esa nota debe imprimir “Reprobado” . 
Requisitos: Las notas que se ingresan pueden tener decimales.
*/
public class Ejercicio_02 {

	public static void main(String[] args) {
		
		float nota_1, nota_2, nota_3; // Creamos 3 variables de tipo float
		
		Scanner entrada;
		entrada = new Scanner(System.in); // Instanciamos un objeto de la clase Scanner
		
		
		System.out.println("\n-- Promedio de notas --\n");
		System.out.print("Ingrese el nombre del alumno: "); // solicitamos el nombre del alumno
		
		String nombre = entrada.nextLine();
		
		System.out.print("Ingrese Nota 1: "); // Solicitamos nota 1
		nota_1 = entrada.nextFloat();
		
		
		System.out.print("Ingrese Nota 2: "); // Solicitamos nota 2
		nota_2 = entrada.nextFloat();
		
		System.out.print("Ingrese Nota 3: "); // Solicitamos nota 3
		nota_3 = entrada.nextFloat();

		float promedio = (nota_1 + nota_2 + nota_3)/3; // Se calcula el promedio y se almacena en la variable 'promedio'
		
		
		
		if (promedio >= 3) { // Construimos una condicional para verificar el estado final del alumno
			System.out.print("\nEl alumno " + nombre + " fue 'Aprobado' con un promedio de: ");
			System.out.printf("%.2f", promedio);
			
			
		} else {
			System.out.print("\nEl alumno " + nombre + " fue 'Reprobado' con un promedio de: ");
			System.out.printf("%.2f", promedio);
			
		}
		
		entrada.close();

	}

}
