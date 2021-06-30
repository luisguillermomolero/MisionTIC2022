// Programa que permite deducir si un número leido por teclado es par.

import java.util.Scanner;

public class ParImpar {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int valor;
        System.out.println("Por favor, introduzca un valor");
        valor = sc.nextInt();
        // condicional "?" ":"
        System.out.println(valor + (valor%2==0 ? " es par " : " es impar ")); 
        sc.close();
    }
}
