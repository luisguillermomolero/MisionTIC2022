package co.edu.utp.misiontic2022.c2.vista;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import co.edu.utp.misiontic2022.c2.controlador.CalculadoraController;
import co.edu.utp.misiontic2022.c2.controlador.Operacion;

public class CalculadoraConsola implements CalculadoraVista {

    private CalculadoraController controller;
    private String numeroUno;
    private String numeroDos;

    private void menuPrincipal() {
        try (var input = new BufferedReader(new InputStreamReader(System.in))) {
            var mainLoop = true;

            while (mainLoop) {
                System.out.println("==============================================");
                System.out.println("************ Calculadora Manual **************");
                System.out.println("==============================================");
                System.out.println(" Puedes realizar operaciones algebraicas:");
                System.out.println(" '+': Suma");
                System.out.println(" '-': Resta");
                System.out.println(" '*': Multiplicación");
                System.out.println(" '/': División");
                System.out.println(" '%': Módulo - Resto de la división");
                System.out.println(" '.': Salir");
                System.out.println("==============================================");
                System.out.print("Ingrese la operación que desea realizar: ");
                var opcion = input.readLine();
                switch (opcion) {
                    case "+":
                        controller.setOperacion(Operacion.SUMA);
                        break;
                    case "-":
                        controller.setOperacion(Operacion.RESTA);
                        break;
                    case "*":
                        controller.setOperacion(Operacion.MULTIPLICACION);
                        break;
                    case "/":
                        controller.setOperacion(Operacion.DIVISION);
                        break;
                    case "%":
                        controller.setOperacion(Operacion.MODULO);
                        break;
                    case ".":
                        System.out.println("Hasta luego!!\n");
                        mainLoop = false;
                        continue;
                    default:
                        System.err.println("Opción '" + opcion + "' no válida");
                        System.out.println("\nPresione ENTER para continuar.");
                        input.readLine();
                        continue;
                }
                System.out.print("Ingrese el primer número: ");
                numeroUno = input.readLine();
                System.out.print("Ingrese el segundo número: ");
                numeroDos = input.readLine();

                controller.actionPerformed(null);

                System.out.println("\nPresione ENTER para continuar.");
                input.readLine();
            }
        } catch (IOException ex) {
            System.err.println("Error en la aplicación: " + ex.getMessage());
        }
    }

    @Override
    public String getNumeroUno() {
        return numeroUno;
    }

    @Override
    public String getNumeroDos() {
        return numeroDos;
    }

    @Override
    public void setResultado(String resultado) {
        System.out.println("Resultado: " + resultado);
    }

    @Override
    public void iniciar(CalculadoraController controller) {
        this.controller = controller;
        menuPrincipal();
    }

    @Override
    public void mostrarExcepcion(Exception ex) {
        System.err.println("Excepción: " + ex.getMessage());
    }

}
