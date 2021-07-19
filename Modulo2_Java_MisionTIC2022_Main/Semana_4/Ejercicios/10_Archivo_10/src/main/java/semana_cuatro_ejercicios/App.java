package semana_cuatro_ejercicios;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.StringTokenizer;

public final class App {

    public static void main(String[] args) {
        try{
            File archivo = new File("Numeros.txt");
            PrintWriter salida = new PrintWriter(archivo);
            if (archivo.exists()) {
                Scanner lector = new Scanner(archivo);
                System.out.println("Números del archivo");
                while (lector.hasNext()) {
                    StringTokenizer numeros = new StringTokenizer(lector.next(), ",");
                    while (numeros.hasMoreTokens()) {
                    System.out.print(numeros.nextToken() + "\t");
                    }
                    System.out.println("");
                }
                salida.close();
                lector.close();
            } else {
                System.out.println("¡El fichero no existe!");
            }
        } catch (IOException e) {
            System.out.println("Ocurrio un ERROR.");
            e.printStackTrace();
        }
    }
}
