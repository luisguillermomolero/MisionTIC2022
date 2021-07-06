package ejercicios_unidad_1;

import java.util.Scanner;

// Elaborado por Mauricio Posada Grupo P72

/*
5. Generar un número aleatorio entre el 1 y el 100, el usuario lo tiene que adivinar 
introduciendo el número por teclado. En el caso que el número a adivinar sea mayor al ingresado, 
decirle al usuario “El número que busca es mayor”, de lo contrario, “El número que busca es menor”. 
El programa finalizará cuando se introduzca el número correcto. Nota: usar la clase Random para generar el número aleatorio.
*/

public class Ejercicio_05 {

	public static void main(String[] args) {
		
		// Creamos un objeto de la clase Scanner
		Scanner entrada;
		entrada = new Scanner(System.in);
		
		// Con el metodo random de la clase Math seleccionamos un numero aleatorio entre 0 y 100
		int numero = (int)(Math.random()*100);
		
		//System.out.println(numero); // Muestra el número secreto... solo para verificar su funcionamiento
		
		// creamos una variable para almacenar el numero introducido por el usuario inicializamos en 0 para que entre al while
		int numero_usuario = 0;
		
		// Solicitamos el numero de oportunidades que quiera el usuario
		System.out.println("\n-- Adivina el número secreto... --");
		System.out.print("Cuantas oportunidades necesitas: ");
		
		// Creamos la variabe intentos para calculara las oprtunidades restantes
		int intentos = entrada.nextInt();
		System.out.println();
		
		// Creamos variable oprtunidades para ir sumando los intentos del usuario
		int oportunidades = 0;
		
		// Mientras el numero introducido sea diferente al numero aleatorio se ejecuta este while
		while (numero_usuario != numero) {
			
			// vamos restando 1 a intentos cada ves que se ejecute el while
			intentos --;
			
			// Incrementamos en 1 cada ves que se ejecute el while
			oportunidades ++;
			
			// Cada ves que numero_usuario se diferente a numero se pide otro numero al usuario
			System.out.print("Introduce un Número entre 1 y 100: ");
			numero_usuario = entrada.nextInt();
			
			
			// Construimos una condicional para dar pistas al usuario, si los intentos no han llegado a 0
			if (intentos > 0) {
				
				if (numero < numero_usuario) {
					
					System.out.println("Debe ser menor a " + numero_usuario);
					
					
				} else if (numero > numero_usuario) {
					
					System.out.println("Debe ser mayor a " + numero_usuario);
					
				} 
				// Si los intentos llegan a cero forzamos la salida del while
			} else if (intentos == 0) {
				
				break;
			}
			
		}
		 // Mostramos el resultado final
		if (numero_usuario == numero) {
			
			System.out.println("\nAdivinaste en " + oportunidades + " intentos!!, el número es el: " + numero);
			
		} else {
			System.out.println("\nPerdiste... el número era el " + numero);
							
		}
		
		entrada.close();


	}

}
