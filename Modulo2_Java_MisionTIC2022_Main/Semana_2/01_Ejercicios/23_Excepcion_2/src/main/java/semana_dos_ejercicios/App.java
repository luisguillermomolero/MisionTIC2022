package semana_dos_ejercicios;

import java.util.InputMismatchException;
import java.util.Scanner;

public class App {
    public static void main(String[] ar) {
        Scanner teclado = new Scanner(System.in);
        int num;
        try {
            System.out.print("Ingrese un valor entero:");
            num = teclado.nextInt();
            int cuadrado = num * num;
            System.out.print("El cuadrado de " + num + " es " + cuadrado);
        } catch (InputMismatchException ex) {
            System.out.println("Debe ingresar obligatoriamente un número entero.");
        }
    }
}