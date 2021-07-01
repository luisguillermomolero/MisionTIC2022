//Realizado por Mauricio Posada. Grupo P72import java.util.Scanner;

import java.util.Scanner;
public class Cliente {

	public static void main(String[] args) {
		
		// Creamos un objeto d ela clase Scanner
		Scanner entrada;
		entrada = new Scanner(System.in);
		
		// Creamos atributos
		String id;
		String nombre;
		String documento;
		String cargo;
		String email;
		String[] nomina = new String[5];
		
		
		// Solicitamos datos al usuario
		System.out.println("\n-- Nomina --\n");
		System.out.print("Ingrese Id: ");
		id = entrada.nextLine();
		
		
		System.out.print("Ingrese Nombre: ");
		nombre = entrada.nextLine();
		
		System.out.print("Ingrese documento: ");
		documento = entrada.nextLine();
		entrada.nextLine();
		System.out.print("Ingrese Cargo: ");
		cargo = entrada.nextLine();
		
		System.out.print("Ingrese Email: ");
		email = entrada.nextLine();
		
		// Incluimos datos en el array
		nomina[0] = id;
		nomina[1] = nombre;
		nomina[2] = documento;
		nomina[3] = cargo;
		nomina[4] = email;
		
		System.out.println();
		
		// Leemos el Array Nomina
		for (String i: nomina) {
			System.out.println(i);
		}
		entrada.close();
	}
}




