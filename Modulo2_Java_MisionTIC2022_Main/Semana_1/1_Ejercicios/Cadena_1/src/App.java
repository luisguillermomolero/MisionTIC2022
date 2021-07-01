//Autor: Adrian F Perez Mesa
//Grupo: 40

import java.util.*;

public class App {

    public static void main(String[] args){
        // var sc = new Scanner(System.in);

        // System.out.println("Introduce un número: ");
        // var numero = sc.nextDouble();
        
        String palabra = "  EstoesunaCadenaDeCarateres ";
        double  item1 = 0;
        
        item1 = palabra.length();
       
        System.out.println("La longitud de la cadena es :"+item1);
        System.out.println("Índice de caracter t:" + palabra.indexOf('t')); 
        System.out.println("Posición de caracter '2':" + palabra.charAt(2)); 
        System.out.println("Devuelve la subcadena desde la posición 1 hasta 6:" + palabra.substring(1,6)); 
        System.out.println("Devuelve la cadena convertida a mayúsculas: " + palabra.toUpperCase());
        System.out.println("Devuelve la cadena convertida a minúsculas: " + palabra.toLowerCase());
        System.out.println("Eliminado espacios " + palabra.trim());
    }
}
