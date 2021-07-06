package semana_dos_ejercicios;

// public class Main {
//     public static void main(String[] args) {
//         Matematicas matematicas=new Matematicas();
//         double c=matematicas.dividir(-1.6, 0);
//         System.out.println("El resultado es" + c);
//     }
// }

public class Main {
    public static void main(String[] args) {
        Matematicas matematicas=new Matematicas();
        try {
            double c=matematicas.dividir(-1.6, 2);
            System.out.println("El resultado es" + c);
        } catch (Exception ex) {
            System.out.println("ERROR -> División por cero ");
        }
    }
}