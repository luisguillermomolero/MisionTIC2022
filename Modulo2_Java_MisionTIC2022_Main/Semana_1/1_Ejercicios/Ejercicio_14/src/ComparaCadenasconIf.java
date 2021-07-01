// Programa que compara cadenas de caracteres con If
public class ComparaCadenasconIf {  
 
    public static void main(String[] args) {
        String cad1="castillo";
        String cad2="casTillo";
        
         //Usando equals
        if(cad1.equals(cad2)){            
            System.out.println("El método equals dice que cad1 es igual a cad2");
        }else{
            System.out.println("El método equals dice que cad1 y cad2 no son iguales");
        }
        
        //Usando equalsIgnoreCase
        if(cad1.equalsIgnoreCase(cad2)){            
            System.out.println("El método equalsIgnoreCase dice que cad1 es igual a cad2");
        }else{
            System.out.println("El método equalsIgnoreCase dice que cad1 y cad2 no son iguales");
        }
        
        System.out.println();
        
        //Usando compareTo
        if(cad1.compareTo(cad2) == 0){            
            System.out.println("El método compareTo dice que cad1 es igual a cad2");
        }else if(cad1.compareTo(cad2) < 0){
            System.out.println("El método compareTo dice que cad1 y cad2 no son iguales. cad1 es menor alfabeticamente");
        }else{
            System.out.println("El método compareTo dice que cad1 y cad2 no son iguales. cad1 es mayor alfabeticamente");
        }
        
        //Usando compareToIgnoreCase
        if(cad1.compareToIgnoreCase(cad2) == 0){            
            System.out.println("El método compareToIgnoreCase dice que cad1 es igual a cad2");
        }else if(cad1.compareToIgnoreCase(cad2) < 0){
            System.out.println("El método compareToIgnoreCase dice que cad1 y cad2 no son iguales. cad1 es menor alfabeticamente");
        }else{
            System.out.println("El método compareToIgnoreCase dice que cad1 y cad2 no son iguales. cad1 es mayor alfabeticamente");
        }        
    }    
}