package ejercicios_unidad_1;

import java.util.Scanner;

// Elaborado por Mauricio Posada Grupo P72

/*
 * 7. Pedir un número, comprobar si es primo y preguntar si quiere introducir más (S/N) y volver a pensar.
 */

public class Ejercicio_07 {

	public static void main(String[] args) {
		
		Scanner entrada;
		entrada = new Scanner(System.in);
		
		
		float numero = 0;
		int contador;
		
		String respuesta;
		boolean pensar = true;
		
		System.out.println("\n-- Averigua si un número es primo --\n");
		
		do {
			
			// Inicializamos contador en cero para que sea 0 siempre que se repita el do while
			contador = 0;
			System.out.println();
			System.out.print("Ingresa un número: ");
			numero = entrada.nextFloat();
			entrada.nextLine();
			
			// Dejamos contador en 0 por defecto con 0 y 1, y contador en 0 cuando el numero es 2
			if (numero == 0 || numero == 1) {
				contador = 1;
			} else if (numero == 2) {
				contador = 0;
			}
			
			
			// Incrementamos contador cada ves que el residuo de una division sea 0
			for (int i = 2; i < numero; i++) {
				
				if (numero % i == 0) {
					
					contador++;
				} 
				
			}
			
			// Si contador es mayor a cero el numero no es primo porque puede ser divisible por algun numero diferente a 1 y por si mismo
			if (contador == 0) {
				
				System.out.println("\nEl número " + (int)numero + " es primo.\n");
			} else {
				
				System.out.println("\nEl número " + (int)numero + " No es primo.\n");
			}
			
			// Validamos la respuesta del usuario para que solo pueda ser S o N, si introduce un valor invalido volvemos a preguntar
			do {
				System.out.print("Quieres intentarlo nuevamente? (S/N): ");
				respuesta = entrada.nextLine();
			} while (respuesta.equalsIgnoreCase("S") == false && respuesta.equalsIgnoreCase("N") == false);
			
			if (respuesta.equalsIgnoreCase("N")) {
				pensar = false;
			} 
		} while (pensar);
		
		// Si la respuesta es N se sale del bucle y despedimos
		
		System.out.println("\nOk, Bye...");
		

		entrada.close();
	}
}	