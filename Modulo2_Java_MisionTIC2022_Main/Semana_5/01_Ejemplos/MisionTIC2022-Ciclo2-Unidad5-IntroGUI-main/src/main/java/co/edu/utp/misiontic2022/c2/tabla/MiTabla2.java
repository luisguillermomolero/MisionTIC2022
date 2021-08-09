package co.edu.utp.misiontic2022.c2.tabla;

import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;

public class MiTabla2 extends JPanel {
    private String titles[];
    private String data[][];

    public MiTabla2() {
        setLayout(new BorderLayout());

        generarDatos();
        var tabla = new JTable(data, titles);
        tabla.setShowHorizontalLines(false);
        tabla.setRowSelectionAllowed(true);
        tabla.setColumnSelectionAllowed(true);
        tabla.setSelectionForeground(Color.white);
        tabla.setSelectionBackground(Color.red);
        add(new JScrollPane(tabla), BorderLayout.CENTER);
    }

    public void generarDatos() {
        // Titles
        titles = new String[8];
        for (int i = 0; i < 8; i++) {
            titles[i] = "Col: " + i;
        }

        // Data
        data = new String[100][8];
        for (int iY = 0; iY < 100; iY++) {
            for (int iX = 0; iX < 8; iX++) {
                data[iY][iX] = "" + iX + "," + iY;
            }
        }
    }

    public static void main(String args[]) {
        JFrame ventana = new JFrame("Tutorial de Java, Swing");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.getContentPane().add(new MiTabla2(), BorderLayout.CENTER);
        ventana.setSize(500, 300);
        ventana.setLocationRelativeTo(null);
        ventana.setVisible(true);
    }
}
