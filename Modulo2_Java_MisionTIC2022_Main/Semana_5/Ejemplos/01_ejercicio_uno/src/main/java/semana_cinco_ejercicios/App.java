package semana_cinco_ejercicios;

import javax.swing.*;

public class App {
    public static void main(String[] args) {
        JFrame marco = new JFrame();// creating instance of JFrame

        JButton boton = new JButton("Clic");// creating instance of JButton
        boton.setBounds(130, 100, 100, 40);// x axis, y axis, width, height

        marco.add(boton);// adding button in JFrame

        marco.setSize(400, 500);// 400 width and 500 height
        marco.setLayout(null);// using no layout managers
        marco.setVisible(true);// making the frame visible
    }
}