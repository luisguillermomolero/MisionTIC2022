package ejercicios_unidad_1;

import java.util.Scanner;

// Elaborado por Mauricio Posada Grupo P72

/*
 * 10.Muestra la serie de fibonacci hasta un número pedido por teclado. 
 * Por ejemplo, si el número ingresado es el 100, debe imprimir 
 * los números 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.
 */

public class Ejercicio_10_obj {

	public static void main(String[] args) {
		
		Scanner entrada;
		entrada = new Scanner(System.in);
		
		Fibonacci serie = new Fibonacci();
		
		System.out.println("\n-- Serie de Fibonacci --\n");
		System.out.print("Ingresa el limite de la serie: ");
		
		int numero = entrada.nextInt();
		
		serie.setNumero(numero);
		
		int limite = serie.getLimite();
		
		
		
		System.out.println();
		System.out.print(serie.num_1 + ", ");
		System.out.print(serie.num_2 + ", ");
		
		while (serie.num_1 + serie.num_2 <= limite) {
			serie.temp = serie.num_1;
			serie.num_1 = serie.num_2;
			serie.num_2 = serie.temp + serie.num_1;
			System.out.print(serie.num_2 + ", ");
		}
		
		entrada.close();

	}

}

class Fibonacci {
	
	private int limite;
	int num_1 = 0;
	int num_2 = 1;
	int temp;
	
	public void setNumero(int numero) {
		this.limite = numero;
	}
	
	public int getLimite() {
		return this.limite;
	}
	
}