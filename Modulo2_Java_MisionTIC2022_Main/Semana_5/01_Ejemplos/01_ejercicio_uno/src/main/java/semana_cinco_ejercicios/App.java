package semana_cinco_ejercicios;

import javax.swing.*;

public class App {
    public static void main(String[] args) {
        JFrame marco = new JFrame();// Creando uns instancia con jframe

        JButton boton = new JButton("Clic");// Creando una instancia con JButton
        boton.setBounds(130, 100, 100, 40);// x axis, y axis, width, height

        marco.add(boton);// Agregando un botón dentro del JFrame

        marco.setSize(400, 500);// 400 width and 500 height
        marco.setLayout(null);// using no layout managers
        marco.setVisible(true);// making the frame visible
    }
}