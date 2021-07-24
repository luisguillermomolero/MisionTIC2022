//Ejemplo de visualización de imagen en el botón:
//https://www.freeiconspng.com/images/register-button-png

package semana_cinco_ejercicios;

import javax.swing.*;

public class App {
    App() {
        JFrame f = new JFrame("Button Example");
        JButton b = new JButton(new ImageIcon("./icon.png"));
        b.setBounds(100, 100, 100, 40);
        f.add(b);
        f.setSize(300, 400);
        f.setLayout(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public static void main(String[] args) {
        new App();
    }
}