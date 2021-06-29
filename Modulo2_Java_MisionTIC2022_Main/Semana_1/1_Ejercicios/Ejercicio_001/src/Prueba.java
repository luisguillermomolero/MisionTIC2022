import java.util.Scanner; //Importa la clase Scanner

public class Prueba {
    public static void main(String[] args) {
        Scanner nsc = new Scanner(System.in);
        System.out.println("Por favor, ingrese un nombre");
        var otroNombre = nsc.nextLine();
        // var otroNombre = "Luis Guillermo";
        var resultado = saludo(otroNombre);
        System.out.println(resultado);
        nsc.close();
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