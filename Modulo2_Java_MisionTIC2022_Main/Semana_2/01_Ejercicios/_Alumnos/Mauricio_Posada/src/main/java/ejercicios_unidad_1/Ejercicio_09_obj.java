package ejercicios_unidad_1;

import java.util.Scanner;

// Elaborado por Mauricio Posada Grupo P72

/*
 * 9. Pide por teclado el nombre, edad y salario y muestra el salario
○ Si es menor de 16 no tiene edad para trabajar
○ Entre 19 y 50 años el salario es un 5 por ciento más
○ Entre 51 y 60 años el salario es un 10 por ciento más
○ Si es mayor de 60 el salario es un 15 por ciento más
 */

public class Ejercicio_09_obj {

	public static void main(String[] args) {
		
		Scanner entrada;
		entrada = new Scanner(System.in);
		
		System.out.println("\n-- Entrevista de trabajo --\n");
		
		Empleado empleado_01 = new Empleado();
		
		System.out.print("Introduzca el nombre del empleado: ");
		String nombre = entrada.nextLine();
		
		System.out.print("Introduzca la edad del empleado: ");
		int edad = entrada.nextInt();
		entrada.nextLine();
		
		
		
		empleado_01.setNombre(nombre);
		System.out.println(empleado_01.getNombre());
		
		empleado_01.setEdad(edad);
		System.out.println(empleado_01.getEdad());
		
		empleado_01.setSalario(edad);
		System.out.println(empleado_01.getSalario());
		
		
		entrada.close();

	}

}

class Empleado {
	
	private String nombre;
	private int edad;
	private double salario;
	
	public Empleado () {
		
		salario = 10000;
		
	}
	
	public void setNombre(String nombre_empleado) {
		this.nombre = nombre_empleado;
	}
	
	public String getNombre() {
		return "\nNombre Empleado: " + nombre;
	}
	
	public void setEdad(int edad_empleado) {
		this.edad = edad_empleado;
	}
	
	public String getEdad() {
		return "La edad del empleado es: " + edad;
	}
	
	public void setSalario(int edad) {
		if (edad < 19) {
			salario = 0;
		}else if (edad > 60) {
			salario += salario*0.15;
		}else if (edad >= 51 && edad <= 60) {
			salario += salario*0.1;
		} else if (edad >= 19 && edad <= 50 ){
			salario += salario*0.05;
		}
			
	}
	
	public String getSalario() {
		if (salario == 0) {
			return "No tiene edad para trabajar.";
		}
		return "El salario del empleado es: $" + salario;
	}
	
}