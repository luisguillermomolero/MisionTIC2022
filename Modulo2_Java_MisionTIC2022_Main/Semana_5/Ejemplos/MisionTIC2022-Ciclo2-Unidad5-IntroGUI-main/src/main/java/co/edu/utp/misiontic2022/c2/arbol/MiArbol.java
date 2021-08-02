package co.edu.utp.misiontic2022.c2.arbol;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTree;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;

public class MiArbol extends JPanel {
    String datos[][] = { 
            { "Colores", "Rojo", "Verde", "Azul" }, 
            { "Sabores", "Salado", "Dulce", "Amargo" },
            { "Longitud", "Corta", "Media", "Larga" }, 
            { "Intensidad", "Alta", "Media", "Baja" },
            { "Temperatura", "Alta", "Media", "Baja" },
            { "Volumen", "Alto", "Medio", "Bajo" }
        };

    static int i = 0;
    DefaultMutableTreeNode raiz, rama, seleccion;
    JTree arbol;
    DefaultTreeModel modelo;

    public MiArbol() {
        setLayout(new BorderLayout());
        raiz = new DefaultMutableTreeNode("raiz");
        arbol = new JTree(raiz);

        add(new JScrollPane(arbol), BorderLayout.CENTER);

        modelo = (DefaultTreeModel) arbol.getModel();

        JButton botonPrueba = new JButton("Cargar información");
        botonPrueba.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                if (i < datos.length) {
                    rama = new Rama(datos[i++]).node();

                    seleccion = (DefaultMutableTreeNode) arbol.getLastSelectedPathComponent();
                    if (seleccion == null) {
                        seleccion = raiz;
                    }

                    modelo.insertNodeInto(rama, seleccion, 0);
                } else {
                    JOptionPane.showMessageDialog(MiArbol.this, "No hay más datos para cargar");
                }
            }
        });

        // Cambio del color del botón
        botonPrueba.setBackground(Color.blue);
        botonPrueba.setForeground(Color.white);
        // Se crea un panel para contener al botón
        JPanel panel = new JPanel();
        panel.add(botonPrueba);
        add(panel, BorderLayout.SOUTH);
    }
}
