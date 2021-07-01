//Escribe un programa java que declare una variable C de tipo entero y asígnale un valor. A continuación muestra un mensaje indicando si el valor de C es positivo o negativo, si es par o impar, si es múltiplo de 5, si es múltiplo de 10 y si es mayor o menor que 100. Consideraremos el 0 como positivo. Utiliza el operador condicional ( ? : ) dentro del println para resolverlo.

public class App {
    public static void main(String[] args) {
       int C = 55;
       System.out.println(C + (C >= 0 ? " es positivo " : " es negativo "));
       System.out.println(C + (C%2== 0 ? " es par " : " es impar "));
       System.out.println(C + (C%5== 0 ? " es múltiplo de 5 " : " no es múltiplo de 5 "));
       System.out.println(C + (C%10== 0 ? " es múltiplo de 10 " : " no es múltiplo de 10"));
       System.out.println(C + (C>100 ? " es mayor que 100 " : " es menor que 100 "));
    }
}