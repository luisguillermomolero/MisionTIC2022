// Programa que declare una variable "B" de tipo entero y asígnale un valor. A continuación muestra un mensaje indicando si el valor de B es positivo o negativo. Consideraremos el 0 como positivo. Utiliza el operador condicional ( ? : ) dentro del println para resolverlo.

 public class Positivo {
    public static void main(String[] args) {                                
      int B = -1;
      //  if (B>=0){
      //    System.out.println(B + " es positivo ");
      //  } else{
      //    System.out.println(B + " es negativo ");
      //  }
      System.out.println(B + (B >= 0 ? " es positivo " : " es negativo "));
    }
}