// // Programa que permite convertir un array en un string

public class DeArrayCad {
    
    public static void main(String[] args) {
        //declaramos un arreglo unidimencional 
        char array1[] = {'H','o','l','a',' ','P','e','p','e'};
        
        //Declaramos tres Variable String
        String cadena, cadena2, cadena3;
        
        //Convertimos usando valueOf()
        cadena = String.valueOf(array1);
        
        //Convertimos usando copyValueOf()
        cadena2 = String.copyValueOf(array1);
        
        //Otra forma valdria también
        cadena3 = new String(array1);
        
        //presentamos las tres cadenas en consola
        System.out.println(cadena);
        System.out.println(cadena2);
        System.out.println(cadena3);
    }    
}