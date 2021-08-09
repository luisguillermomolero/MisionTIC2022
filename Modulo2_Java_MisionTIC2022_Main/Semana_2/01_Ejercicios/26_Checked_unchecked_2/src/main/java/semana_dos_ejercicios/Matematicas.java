//Las excepciones Unchecked son aquellas que no se declaran en el método y que no obligan al que lo llama a hacer un tratamiento de dicha excepción.

package semana_dos_ejercicios;

public class Matematicas {
    public double dividir(double a, double b) {
        if (b == 0) {
            throw new RuntimeException("El argumento b no puede ser 0");
        }
        return a / b;
    }
}