package ejercicios_unidad_1;

import java.util.Scanner;

// Elaborado por Mauricio Posada Grupo P72

/* 1. Realizar la suma, la resta, la división y la multiplicación de dos números leídos por teclado y mostrar 
 * en pantalla “La <operación> de <número 1> y <número 2> es igual a <resultado> ”. */

public class Ejercicio_01 {

	public static void main(String[] args) {
		
		Scanner entrada;
		entrada = new Scanner(System.in); // Creamos un objeto de la clase scanner
		
		System.out.println("\n-- Operaciones Aritméticas --\n");
		System.out.print("Ingrese Número 1: "); // Solicitamos primer numero
		float numero_1 = entrada.nextFloat();
		System.out.print("Ingrese Número 2: "); // Solicitamos Segundo numero
		float numero_2 = entrada.nextFloat();
		
		int resultado_suma = (int)numero_1 + (int)numero_2; // Realizamos las operaciones correspondientes
		int resultado_resta = (int)numero_1 - (int)numero_2;
		int resultado_multiplicacion = (int)numero_1 * (int)numero_2;
		float resultado_division = numero_1 / numero_2;
		
		
		// Mostramos resultados en consola
		System.out.println("\nLa Suma de " + numero_1 + " y " + numero_2 + " es igual a: 		" + resultado_suma); 
		System.out.println("La Resta de " + numero_1 + " menos " + numero_2 + " es igual a: 		" + resultado_resta);
		System.out.println("La Multiplicación de " + numero_1 + " por " + numero_2 + " es igual a: 	" + resultado_multiplicacion);
		System.out.println("La División de " + numero_1 + " entre " + numero_2 + " es igual a: 	" + resultado_division);

		entrada.close();
		
	}

}
