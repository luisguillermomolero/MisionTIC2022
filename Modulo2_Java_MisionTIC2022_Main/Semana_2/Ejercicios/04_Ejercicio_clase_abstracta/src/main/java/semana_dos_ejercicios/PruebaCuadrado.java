package semana_dos_ejercicios;

import java.util.Scanner;

public class PruebaCuadrado
{
    //Método principal de java
    public static void main(String[] args)
    {
        //Declaración de variables
        String colorDelCuadrado;
        double ladoDelCuadrado;

        //Se instancia a la variable "Scanner"
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduzca el color del cuadrado: ");
        colorDelCuadrado = sc.nextLine();

        System.out.print("Introduzca el lado del cuadrado: ");
        ladoDelCuadrado = sc.nextDouble();

        Cuadrado cuadrado1 = new Cuadrado(colorDelCuadrado, ladoDelCuadrado);

        System.out.printf("El área del cuadrado %s es: %f", cuadrado1.getColor(), cuadrado1.calcularArea());
        sc.close();
    }
}