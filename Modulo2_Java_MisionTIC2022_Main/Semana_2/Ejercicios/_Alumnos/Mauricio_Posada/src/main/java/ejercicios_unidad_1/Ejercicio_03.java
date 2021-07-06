package ejercicios_unidad_1;

import java.util.Scanner;

// Elaborado por Mauricio Posada Grupo P72

/*
3. Realizar un programa que calcule el sueldo de un trabajador, el programa solicita el número de horas 
que has trabajado en un mes, las horas se pagan a $30.000.
*/

public class Ejercicio_03 {

	public static void main(String[] args) {
		
		
		// Creamos variables necesarias
		int horas_trabajadas;
		float sueldo;
		
		//Creamos constante HORA
		final int HORA = 30000;
		
		// Creamos objeto de la clase Scanner
		Scanner entrada;
		entrada = new Scanner(System.in);
		
		// Solicitamos numero de horas y almacenamos en la variable horas_trabajadas
		System.out.println("\n-- Calcular Sueldo --\n");
		System.out.print("Ingresa el numero de horas trabajadas: ");
		horas_trabajadas = entrada.nextInt();
		
		// Realizamos la operacion
		sueldo = horas_trabajadas * HORA;
		
		
		// Mostramos resultados
		System.out.print("\nEl sueldo del trabajador es: $");
		System.out.printf("%,1.2f", sueldo);
		System.out.println(" pesos.");

		entrada.close();
		

	}

}
