package semana_dos_ejercicios;

import java.util.*;
/**Clases en Java
 * <modificador> class <Nombre clase>{
 *  <Atributos>
 *  <Constructores>
 *  <Métodos>
 * }
 * 
 * public: todos tienen acceso
 * final: Unica clase sin subclases
 * 
 * Constructor por defecto, como?... tiene el mismo nombre de la clase
 * 
 */

 //Nombre de la clase que se explica por si solo; CamelCase. Mismo nombre que el archivo.java
 public class MiPrimeraClase { 
    
    /**Atributos: de primero, 1 por linea, inician en Mayúscula, declarar "private".
    *  Modif-Acceso: public, private, protected, final, static (var de clase), <sm>
    *  wrapper class = Tipo de dato inicia en Mayúscula, envuelve y convierte datos primitivos en objetos.
    */
    // private static final Double PI = 3.1416;
    // private Integer contador = 0;

    //Constructor por defecto

    private MiPrimeraClase(String nombre) {
    }

    //Métodos

    /** <modificador> <retorno> <nombre>(<tipoDato parametros>)
     * {
     *      <sentencias>
     * }
    */

    public String metodoString(int n) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número para sumarle a cinco: ");
        int numero = sc.nextInt();
        sc.close();
        return "Método metodoString. \n El resultado es: " + (n + numero);
    }

    public String metodoEntero(){
        int suma = 5+5;
        return "\nMétodo \"metodoEntero\" \n El resultado es: " + suma;
    }
    
    public int metodoEnteroDos(){
        int sumaDos = 5+5;
        return sumaDos;
    }

    int MetodoEnteroTres(){
        int sumaDos = 20+20;
        return sumaDos;
    }


    // public void incrementarContador(Integer y) {
    //     contador += y;
    //     }

    //Método principal de java
    public static void main(String[] args) {
        System.out.println("Hello World!");

        //Instanciar la clase "MiPrimeraClase" para llamar a sus métodos
        MiPrimeraClase ejemplos = new MiPrimeraClase("Constructor\n");
        
        System.out.println(ejemplos.metodoString(5));
        System.out.println(ejemplos.metodoEntero());
        
        System.out.println("\nMétodo \"metodoEnteroDos\"\n El resultado es: " + ejemplos.metodoEnteroDos());
        System.out.println("\nMétodo \"metodoEnteroTres\"\n El resultado es: " + ejemplos.MetodoEnteroTres());
    }
}
