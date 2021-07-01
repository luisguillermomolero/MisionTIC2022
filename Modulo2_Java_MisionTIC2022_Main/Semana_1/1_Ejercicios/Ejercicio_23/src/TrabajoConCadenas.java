// Programa que convierte un número en un String o cadena

public class TrabajoConCadenas {
    public static void main(String[] args) {
        
        //Declaración de variables
        double d = 858.48;
        int i = 20;
        byte b =19;        
        String cad1,cad2,cad3;        
        
        //Convertimos a String cada variable usando toString
        cad1 = Double.toString (d);        
        cad2 = Integer.toString (i);
        cad3 = Byte.toString(b);
        
        
        //Sumamos 1 detrás de cad1 
        System.out.println ("Aquí se realiza una concatenación de ("+cad1+" + 1) con resultado: ("+ (cad1 + 1)+")");
        
                
        //Sumamos 1 delante de cad1 
        System.out.println ("Aquí se realiza una concatenación de (1 + "+cad1+") con resultado: ("+ (1 + cad1)+")");
        
        //Sumamos 1 a la variable double "d"
        System.out.println ("Aquí se realiza una suma de 1 + "+d+" con resultado: "+ (1 + d));
          
        //Concatenamos cad2 y cad3
        System.out.println ("Aquí se realiza una concatenación de cad2 + cad3 con resultado: "+ (cad2 + cad3));
    }
    
}