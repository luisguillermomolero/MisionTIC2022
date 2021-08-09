package co.edu.utp.misiontic2022.c2.cdiaz.util;

import java.io.BufferedReader;
import java.io.IOException;

/**
 * InputUtilities
 */
public class InputUtilities {

    public static String inputValidString(BufferedReader input, String message) throws IOException {
        return inputValidString(input, message, null);
    }

    public static String inputValidString(BufferedReader input, String message, String defaultValue)
            throws IOException {
        String value;
        do {
            System.out.print(message);
            value = input.readLine();
            if (value.isBlank()) {
                System.err.println("Entrada inválida, intenta de nuevo");
                value = null;
            }
        } while (value == null);
        return value;
    }

    public static Integer inputValidInteger(BufferedReader input, String message) throws IOException {
        return inputValidInteger(input, message, null);
    }

    public static Integer inputValidInteger(BufferedReader input, String message, Integer defaultValue)
            throws IOException {
        Integer value;
        do {
            System.out.print(message);
            var text = input.readLine();
            try {
                value = Integer.valueOf(text);
            } catch (Exception e) {
                System.err.println("Entrada inválida, intenta de nuevo");
                value = defaultValue;
            }
        } while (value == null);
        return value;
    }

    public static void waitForEnter(BufferedReader input) throws IOException{
        waitForEnter(input, "\nPresione ENTER para continuar");
    }

    public static void waitForEnter(BufferedReader input, String message) throws IOException{
        System.out.println(message);
        input.readLine();

    }
}