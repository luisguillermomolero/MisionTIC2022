package co.edu.utp.misiontic2022.c2.cdiaz.view;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MainMenu {

    public static void start() {
        var mainLoop = true;
        var input = new BufferedReader(new InputStreamReader(System.in));
        do {
            System.out.println();
            System.out.println("==========================================");
            System.out.println(" Bienvenido al Gestor de recursos humanos");
            System.out.println("==========================================");
            System.out.println("1. Gestión de empleados");
            System.out.println("0. Salir");
            System.out.println("==========================================");
            System.out.print("Ingrese su opción: ");
            try {
                var opcion = Integer.valueOf(input.readLine());
                switch (opcion) {
                    case 0:
                        mainLoop = false;
                        break;
                    case 1:
                        EmployeeMenu.start();
                        break;
                    default:
                        System.err.println("Opción no válida");
                }
            } catch (NumberFormatException | IOException e) {
                System.err.println("Ha ocurrido un error: " + e);
            }
        } while (mainLoop);
        System.out.println("\nGracias por usar nuestros servicios");
    }
}
