//Autor: Adrian F Perez Mesa
//Grupo: 40

import java.util.*;

public class App {

    public static void main(String[] args){
        var sc = new Scanner(System.in);

        System.out.println("Introduce un número: ");
        var numero = sc.nextDouble();

        var digitos = numeroDigitos(numero);
        System.out.println(digitos);
        sc.close();
    }

    public static String numeroDigitos(double numero){
        double doble = 0;
        double triple = 0;

        doble = Math.pow(numero,2);
        triple = Math.pow(numero,3);

        String dos = String.valueOf(doble);
        String tres = String.valueOf(triple);

        return "El doble es: " + dos + "\n" + "El triple es: " + tres;
        
    }
    
}