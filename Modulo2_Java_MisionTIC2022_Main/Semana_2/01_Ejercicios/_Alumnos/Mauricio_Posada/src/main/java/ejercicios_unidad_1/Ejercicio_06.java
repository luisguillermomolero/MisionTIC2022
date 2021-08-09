package ejercicios_unidad_1;


// Elaborado por Mauricio Posada Grupo P72

/*
 * 6. Realiza un programa que solicite el sexo (H/M) y la altura (cm) al usuario y que calcule el peso ideal.
 	peso ideal mujeres = altura - 120
 	peso ideal hombres = altura - 110
 */

import javax.swing.JOptionPane;

public class Ejercicio_06 {

	public static void main(String[] args) {
		
		String genero;
		
		// Solicitamos el genero del usuario validando que se introduzca correctamente, si no es asi se vuelve a solicitar
		do {
			
			// Se va a usar interfaz grafica con JOption Pane
			genero = JOptionPane.showInputDialog(null, "Cual es tu género? (M o F): ", "Averigua tu peso ideal!!", JOptionPane.QUESTION_MESSAGE);
			
			
			
		} while (genero.equalsIgnoreCase("M") == false && genero.equalsIgnoreCase("F") == false);

		
		int altura = 0;
		int pesoIdeal = 0;
		
		// Solicitamos la altura al usuario
		altura = Integer.parseInt(JOptionPane.showInputDialog("Cual es tu altura en cm?: ", altura));
		
		// Se verifica la condicoin del genero y se realiza la operacion correspondiente
		if (genero.equalsIgnoreCase("M")) {
			
			pesoIdeal = altura - 110;
			
		} else {
			
			pesoIdeal = altura - 120;
			
		}
		// Mostramos el resultado
		JOptionPane.showMessageDialog(null, "Tu peso ideal es: " + pesoIdeal + "Kg.");
		
	}

}
