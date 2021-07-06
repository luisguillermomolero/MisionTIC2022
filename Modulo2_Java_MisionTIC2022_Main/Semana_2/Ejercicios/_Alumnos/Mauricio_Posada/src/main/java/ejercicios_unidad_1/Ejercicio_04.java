package ejercicios_unidad_1;

import java.util.Scanner;

// Elaborado por Mauricio Posada Grupo P72

/*
4. Solicitar un número al usuario y mostrar la tabla de multiplicar de ese número, 
desde el 0 hasta el 10. Truco: Usa un bucle for para recorrer la tabla y mostrar los datos.
*/

public class Ejercicio_04 {

	public static void main(String[] args) {
		
		// creamos un objeto de la clase Scanner
		Scanner entrada;
		entrada = new Scanner(System.in);
		
		int numero;
		
		// solicitamos un numero al usuario
		System.out.println("\n-- La tabla de multiplicar que quieras!! --\n");
		System.out.print("Ingresa un número: ");
		numero = entrada.nextInt();
		System.out.println();
		
		
		// Realizamos un for para multiplicar el numero dado por cada indice
		for (int i = 0; i <= 10; i++) {
			System.out.println(numero + " x " + i + " = " + numero*i);
		}

		entrada.close();

	}

}
