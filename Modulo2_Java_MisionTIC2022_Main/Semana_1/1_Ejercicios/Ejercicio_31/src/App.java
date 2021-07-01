//Realizado por: Adrian Felipe Perez Mesa: Grupoo P40
import java.util.*;

public class App {
    public static void main(String[] args){
        var sc = new Scanner(System.in);
        System.out.println("Introduzca un número entero: ");
        var numero = sc.nextInt();
        var resultado = parImpar(numero);
        System.out.println(resultado);
        sc.close();
    }
    public static String parImpar(int numero){
        return numero%2==0 ? "Es Par": "Es impar"; 
    }
}