/* Swing - JMenuBar, JMenu, JMenuItem
 * 
 *  Cuando necesitamos implementar un menú horizontal en 
 *  la parte superior de un JFrame requerimos de un objeto 
 *  de la clase JMenuBar, uno o más objetos de la clase JMenu 
 *  y por último objetos de la clase JMenuItem.
 *  
 *  Par la captura de eventos debemos implementar la interface 
 *  ActionListener y asociarlo a los controles de tipo JMenuItem, 
 *  el mismo se dispara al presionar con el mouse el JMenuItem.
 *  
 *  Problema: Confeccionaremos un menú de opciones que contenga 
 *  tres opciones que permita cambiar el color de fondo del JFrame 
 *  a los colores: rojo, verde y azul.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Formulario extends JFrame implements ActionListener{
    private JMenuBar mb;
    private JMenu menu1;
    private JMenuItem mi1,mi2,mi3;
    public Formulario() {
        setLayout(null);
        mb=new JMenuBar();
        setJMenuBar(mb);
        menu1=new JMenu("Opciones");
        mb.add(menu1);
        mi1=new JMenuItem("Rojo");
        mi1.addActionListener(this);
        menu1.add(mi1);
        mi2=new JMenuItem("Verde");
        mi2.addActionListener(this);
        menu1.add(mi2);
        mi3=new JMenuItem("Azul");
        mi3.addActionListener(this);
        menu1.add(mi3);               
    }
    
    public void actionPerformed(ActionEvent e) {
    	Container f=this.getContentPane();
        if (e.getSource()==mi1) {
            f.setBackground(new Color(255,0,0));
        }
        if (e.getSource()==mi2) {
            f.setBackground(new Color(0,255,0));
        }
        if (e.getSource()==mi3) {
            f.setBackground(new Color(0,0,255));
        }        
    }
    
    public static void main(String[] ar) {
        Formulario formulario1=new Formulario();
        formulario1.setBounds(10,20,300,200);
        formulario1.setVisible(true);
        formulario1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }    
}