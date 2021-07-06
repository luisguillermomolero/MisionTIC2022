package ejercicios_unidad_1;

import java.util.Scanner;


// Elaborado por Mauricio Posada Grupo P72

/*
 * Realizar un programa que permita controlar el juego de piedra, papel, tijera 
 * introduciendo P para piedra, L para papel y T para tijera por cada jugador.
 */

public class Ejercicio_08 {

	public static void main(String[] args) {
		
		Scanner entrada;
		entrada = new Scanner(System.in);
		
		String respuesta;
		boolean pensar = true;
		
		System.out.println("\n-- Piedra, Papel o Tijera --\n");
		
		String[] jugada = new String[2];
		
		do {
		
		for (int i = 0; i < jugada.length;i++) {
			
			do {
				// solicitamos las opciones a los jugadores
				System.out.print("Jugador " +  (i+1) + " (Piedra: P, Papel: L, Tijera: T): ");
				jugada[i] = entrada.nextLine();
				
			} while ((jugada[i].equalsIgnoreCase("P") == false) && (jugada[i].equalsIgnoreCase("L") == false) 
					&& (jugada[i].equalsIgnoreCase("T") == false));
			
		}
		
		// Utilizamos una condicional para verificar quien gana
		
		if (jugada[0].equalsIgnoreCase(jugada[1])) {
			
			System.out.println("\nEl juego esta empatado!!");
			
		} else {
			
			if(jugada[0].equalsIgnoreCase("P") && jugada[1].equalsIgnoreCase("l")) {
				System.out.println("\nHa ganado el Jugador 2");
			} else if(jugada[0].equalsIgnoreCase("L") && jugada[1].equalsIgnoreCase("P")) {
				System.out.println("\nHa ganado el Jugador 1");
			} else if(jugada[0].equalsIgnoreCase("P") && jugada[1].equalsIgnoreCase("T")) {
				System.out.println("\nHa ganado el Jugador 1");
			} else if(jugada[0].equalsIgnoreCase("t") && jugada[1].equalsIgnoreCase("p")) {
				System.out.println("\nHa ganado el Jugador 2");
			} else if(jugada[0].equalsIgnoreCase("t") && jugada[1].equalsIgnoreCase("l")) {
				System.out.println("\nHa ganado el Jugador 1");
			} else if(jugada[0].equalsIgnoreCase("l") && jugada[1].equalsIgnoreCase("t")) {
				System.out.println("\nHa ganado el Jugador 2");
			}
		}
		
		// Preguntamos si se quiere jugar nuevamente con validacion de respuestas
		do {
			System.out.print("\nQuieres Jugar nuevamente? (S/N): ");
			respuesta = entrada.nextLine();
		} while (respuesta.equalsIgnoreCase("S") == false && respuesta.equalsIgnoreCase("N") == false);
		
		if (respuesta.equalsIgnoreCase("N")) {
			pensar = false;
		} 
	} while (pensar);
		
		System.out.println("\nOk, Bye!!");

		entrada.close();

	}

}
