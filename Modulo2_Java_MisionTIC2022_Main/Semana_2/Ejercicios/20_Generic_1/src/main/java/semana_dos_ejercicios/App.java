package semana_dos_ejercicios;

//Clase genérica.

/**En su esencia, el término genéricos significa tipos parametrizados. Los tipos parametrizados son importantes porque le permiten crear clases, interfaces y métodos en los que el tipo de datos sobre los que operan se especifica como parámetro. Una clase, interfaz o método que funciona con un tipo de parámetro se denomina genérico, como una clase genérica o método genérico. */

//T es un parámetro de tipo que será reemplazado por un tipo real cuando se crea un objeto de tipo Gen.

class Gen<T>{
    //T es el parámetro de tipo genérico.
    T ob; //Declara un objeto de tipo T

    //Pase al constructor una referencia a un objeto de tipo T.
    Gen(T o){
        ob=o;
    }

    T getOb(){
        return ob;
    }

    //Muestra el tipo de T
    void mostrarTipo(){
        System.out.println("El tipo de T es: "+ob.getClass().getName());
    }
}

//Demostración de clase genérica
class Genericos {
    public static void main(String[] args) {

        //Crea una referencia Gen para Integers.
        Gen<Integer> iOb;

        //Cree un objeto Gen<Integer> y asigne su referencia a iOb.
        //Observe el uso de autoboxing para encapsular el valor 28 dentro de un objeto Integer.
        iOb=new Gen<Integer>(28);

        //Muestra el tipo de dato utilizado por iOb
        iOb.mostrarTipo();

        //Obtenga el valor en iOb.
        //Fíjese que no se necesita una conversión
        int v=iOb.getOb();
        System.out.println("Valor: "+v);
        System.out.println();

        //Cree un objeto Gen para Strings.
        Gen<String> strOb=new Gen<String>("Prueba de genéricos");

        //Muestra el tipo de dato utilizado por strOb
        strOb.mostrarTipo();

        //Obtenga el valor de strOb.
        // De nuevo, note que no se necesita de conversión
        String str=strOb.getOb();
        System.out.println("Valor: "+str);
    }
}