package semana_dos_ejercicios;

//JOptionPane:Clase que permite mostrar dialogos gráficos. Permite introducir/mostrar información y se encuentra en el paquete javax.swing.
import javax.swing.JOptionPane;

public class EjercicioVector1 {

    
  public static void main(String[] args) {
        
    //declaramos un array
    String[] Numero = new String[]{"1","2","3","4","5"};

    //Muestra los datos del array <showMessageDialog(parentComponent,Object message)
    JOptionPane.showMessageDialog(null, Numero);
  }
}