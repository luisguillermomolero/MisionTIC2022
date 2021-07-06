package semana_dos_ejercicios;

public class App {

    public static void main (String [] args)     {
        try {
            System.out.println("Intentamos ejecutar el bloque de instrucciones:");
            System.out.println("Instrucción 1.");
            int n = Integer.parseInt("M"); //error forzado en tiempo de ejecución.
            System.out.println("Instrucción 2.");
            System.out.println("Instrucción 3, etc.");
        }
        catch (Exception e) {
            System.out.println("Instrucciones a ejecutar cuando se produce un error");
        }
        finally {
            System.out.println("Instrucciones a ejecutar finalmente tanto si se producen errores como si no.");

        }

    }

}