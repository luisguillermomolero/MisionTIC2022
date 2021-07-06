//Las excepciones Checked son aquellas que deben declararse en el método mediante la palabra throws y que obligan al que lo llama a hacer un tratamiento de dicha excepción.

package semana_dos_ejercicios;

public class App {
    public static void main(String[] args) throws Exception {
        Matematicas matematicas=new Matematicas();
        double c = matematicas.dividir(24, 2);
        System.out.println("El resultado es " + c);
    }
}

