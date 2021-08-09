package co.edu.utp.misiontic2022.c2.tabla;

import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;

public class MiTabla extends JPanel {

    public MiTabla() {
        setLayout(new BorderLayout());
        JTable tabla = new JTable(new ModeloDatos());
        JScrollPane panel = new JScrollPane(tabla);
        add(panel, BorderLayout.CENTER);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Tutorial de Java, Swing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new MiTabla(), BorderLayout.CENTER);
        frame.setSize(400, 150);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
