// Programa para deducir si un número leido desde una variable es par o impar

import java.util.*;

public class ParImpar {
    public static void main(String[] args) {
        
        var sc = new Scanner(System.in);
        int valor;
        System.out.println("Por favor, introduzca un valor");
        valor = sc.nextInt();
        System.out.println(valor + (valor%2==0 ? " es par " : " es impar ")); // ? :
        sc.close();
    }
}
