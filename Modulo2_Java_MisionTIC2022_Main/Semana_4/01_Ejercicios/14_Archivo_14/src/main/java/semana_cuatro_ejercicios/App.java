//Programa que lee el contenido del archivo creado en el ejercicio anterior

package semana_cuatro_ejercicios;

import java.io.DataInputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class App {
    public static void main(String[] args) {
        FileInputStream fis = null;
        DataInputStream entrada = null;
        int n;
        try {
            fis = new FileInputStream("datos.dat");
            entrada = new DataInputStream(fis);
            while (true) {
                n = entrada.readInt(); // se lee un entero del fichero
                System.out.println(n); // se muestra en pantalla
            }
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        } catch (EOFException e) {
            System.out.println("Fin de fichero");
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            try {
                if (fis != null) {
                    fis.close();
                }
                if (entrada != null) {
                    entrada.close();
                }
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}