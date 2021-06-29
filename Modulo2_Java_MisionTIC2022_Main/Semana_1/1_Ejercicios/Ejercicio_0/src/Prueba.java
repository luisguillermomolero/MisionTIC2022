import java.util.Scanner; //Importa la clase Scanner

public class Prueba {
    public static void main(String[] args) {
        System.out.print("Hola Mundo \n");

        var sc = new Scanner(System.in); //si no existe un sc.close() muestra un warning
        System.out.println("Por favor ingrese su nombre");
        var nombre = sc.nextLine(); //nextInt(); nextFloat(); nextDouble();
        
        System.out.println("Hola " + nombre + "!");
        
        System.out.print("Por favor, introduzca un número :");
        int numero = sc.nextInt(); //si no existe un sc.close() muestra un warning
        //sc.close();

        int i = 0;
        for (i = 0; i <= numero; i++){
            System.out.println("El For va de i = " + i + " hasta " + numero);
            if (i == numero){
                System.out.println("Hasta aquí llego el ejercicio");
            }
        }
        
        int n = 0;
        do{
            System.out.println("El do-while va de n = " + n + " hasta " + numero);
            n = n+1;
        } while(n <= numero);

        int s = 0;
        while (s <= numero){
            System.out.println("El while va de s = " + s + " hasta " + numero);
            s = s+1;
        }

        //fragmento de código que va a trabajar con el método saludo()
        
        Scanner nsc = new Scanner(System.in);
        System.out.println("Por favor, ingrese un nombre");
        var otroNombre = nsc.nextLine();
        // var otroNombre = "Luis Guillermo";
        var resultado = saludo(otroNombre);
        System.out.println(resultado);
    }
    
    /*Parametros de los métodos 
        Modificadores de acceso: 
            public
            private
            protected
            default
        Retornos: 
            void: Un método sin ningún valor de retorno.
        Directivas: 
            static: Significa que el método pertenece a la clase Main

        <modificador de acceso> <directiva> <tipo_dato> <nombre_metodo(tipo nombre_var, tipo nombre_var...)>{}
        */

    public static String saludo(String otroNombre){
        return "Hola " + otroNombre + "!";
    }
}