package semana_dos_ejercicios;

import java.util.Scanner;

public class PruebaTriangulo
{
    //Método principal de java
    public static void main(String[] args)
    {
        //Declaración de variables
        String colorDelTriangulo;
        double baseDelTriangulo;
        double alturaDelTriangulo;

        //Se instancia a la variable "Scanner"
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduzca el color del triángulo: ");
        colorDelTriangulo = sc.nextLine();

        System.out.print("Introduzca la base del triángulo: ");
        baseDelTriangulo = sc.nextDouble();

        System.out.print("Introduzca la altura del triángulo: ");
        alturaDelTriangulo = sc.nextDouble();

        Triangulo triangulo1 = new Triangulo(colorDelTriangulo, baseDelTriangulo, alturaDelTriangulo);

        System.out.printf("El área del triángulo %s es: %f", triangulo1.getColor(), triangulo1.calcularArea());
        sc.close();
    }
}