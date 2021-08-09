package semana_cuatro_ejercicios;

import java.io.*;

public class App {
    public static void main(String args[]) {
        byte[] buffer = new byte[255];
        System.out.println("\nEscribe el texto: ");
        try {
            System.in.read(buffer, 0, 255);
        } catch (IOException e) {
            System.err.println(e);
        }
        System.out.println("\nLa línea escrita es: ");
        System.out.println(new String(buffer));
    }
}