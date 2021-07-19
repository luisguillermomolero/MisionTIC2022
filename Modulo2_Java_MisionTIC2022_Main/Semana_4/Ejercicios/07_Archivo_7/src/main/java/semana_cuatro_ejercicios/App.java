package semana_cuatro_ejercicios;

// El siguiente ejemplo abre un archivo de registro. Si no existe el archivo, se crea. Si el archivo existe, se abre para agregarlo.

import static java.nio.file.StandardOpenOption.*;
import java.nio.file.*;
import java.io.*;

public class App {

  public static void main(String[] args) {

    // Convert the string to a
    // byte array.
    String s = "Hola Mundo! ";
    byte data[] = s.getBytes();
    Path p = Paths.get("./logfile.txt");

    try (OutputStream out = new BufferedOutputStream(
      Files.newOutputStream(p, CREATE, APPEND))) {
      out.write(data, 0, data.length);
      System.out.print("Archivo creado");
    } catch (IOException x) {
      System.err.println(x);
    }
  }
}