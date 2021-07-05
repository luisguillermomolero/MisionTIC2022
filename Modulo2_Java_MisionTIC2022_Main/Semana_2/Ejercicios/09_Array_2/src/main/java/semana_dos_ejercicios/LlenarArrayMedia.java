package semana_dos_ejercicios;

import javax.swing.JOptionPane;


public class LlenarArrayMedia {

    
  public static void main(String[] args) {

    int valor = 0;
    valor= Integer.parseInt(JOptionPane.showInputDialog("Ingrese cantidad de elementos para el promedio"));

    int [] numeros = new int[valor];
    // Declaracion variable
    int suma = 0;
    double promedio;
      
    //ingresaNumero
    for (int i=0;i<valor; i++){
      numeros[i]=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el Numero \n" + (i+1) + " por favor"));
      suma += numeros[i];
    }
    //operacion
    promedio=(double)suma/numeros.length;
    
    //mostrarDatos
    JOptionPane.showMessageDialog(null, promedio);
  }
}