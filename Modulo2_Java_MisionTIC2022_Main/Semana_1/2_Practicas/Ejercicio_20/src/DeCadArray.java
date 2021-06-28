// Programa que permite convertir un String en un array y un array en un string

public class DeCadArray {
    
    public static void main(String[] args) {
        //declaramos una cadena
        String cadena = "Hola Pepe";
        
        //Declaramos un array
        char car1[];
        
        //Llenamos el array con la cadena
        car1 = cadena.toCharArray();
        
        //Recorremos el array a nuestro antojo
        for(int i=0;i<car1.length/2;i++){
            System.out.println(car1[i]); 
        }
        for(int i=car1.length/2;i<car1.length;i++){
            System.out.print(car1[i]+" "); 
        }
        
        System.out.println(); 
    }    
}
 