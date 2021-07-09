package semana_dos_ejercicios;

import javax.swing.JOptionPane;

public class LlenarArrayMedia {

    
  public static void main(String[] args) {

    // Declaracion variable
    int suma = 0;
    double promedio;
    int valor = 0;

    valor= Integer.parseInt(JOptionPane.showInputDialog("Ingrese cantidad de elementos para el calculo del promedio"));

    //defino el arreglo de acuerdo a valor
    int [] numeros = new int[valor];
       
      
    //Llenar el arreglo de acuerdo a valor
    for (int i=0;i<valor; i++){
      //Solicitando dato a dato hasta valor
      numeros[i]=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el Numero \n" + (i+1) + " de " + valor + " por favor"));
      suma += numeros[i];
    }
    //operacion
    promedio=(double)suma/numeros.length;
    
    //mostrarDatos
    JOptionPane.showMessageDialog(null, promedio);
  }
}