/*Crea una miniencuesta gráfica. Daremos una serie de opciones para que el usuario elija. La encuesta preguntará lo siguiente:

*Elije un sistema operativo (solo una opción, JRadioButton)
    *Windows
    *Linux
    *Mac
*Elije tu especialidad (pueden seleccionar ninguna o varias opciones, JCheckBox)
    *Programación
    *Diseño gráfico
    *Administración
Horas dedicadas en el ordenador (usaremos un slider entre 0 y 10)
*/

package semana_cinco_ejercicios;

import javax.swing.ButtonGroup;
import javax.swing.JCheckBox;
import javax.swing.JOptionPane;
import javax.swing.JRadioButton;
 
/**
 * @author DiscoDurodeRoer
 */
public class MiniEncuestaApp extends javax.swing.JFrame {

    private javax.swing.JButton btnGenerar;
    private javax.swing.JCheckBox ckbAdministracion;
    private javax.swing.JCheckBox ckbDiseno;
    private javax.swing.JCheckBox ckbProgramacion;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JSeparator jSeparator2;
    private javax.swing.JLabel lblHoras;
    private javax.swing.JRadioButton rdbLinux;
    private javax.swing.JRadioButton rdbMac;
    private javax.swing.JRadioButton rdbWindows;
    private javax.swing.JSlider sldHoras;
 
    public MiniEncuestaApp() {
        initComponents();
         
        //Creamos una instacia de ButtonGroup
        ButtonGroup btg=new ButtonGroup();
         
        //Añadimos los botones radiobutton
        //Si no lo hacemos, los botones seran independientes
        btg.add(rdbWindows);
        btg.add(rdbLinux);
        btg.add(rdbMac);
         
    }
 
     
    private void initComponents() {
 
        rdbWindows = new javax.swing.JRadioButton();
        rdbLinux = new javax.swing.JRadioButton();
        rdbMac = new javax.swing.JRadioButton();
        jLabel1 = new javax.swing.JLabel();
        ckbProgramacion = new javax.swing.JCheckBox();
        jLabel2 = new javax.swing.JLabel();
        ckbDiseno = new javax.swing.JCheckBox();
        ckbAdministracion = new javax.swing.JCheckBox();
        jSeparator1 = new javax.swing.JSeparator();
        btnGenerar = new javax.swing.JButton();
        jSeparator2 = new javax.swing.JSeparator();
        sldHoras = new javax.swing.JSlider();
        jLabel3 = new javax.swing.JLabel();
        lblHoras = new javax.swing.JLabel();
 
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Mini Encuesta");
 
        rdbWindows.setText("Windows");
 
        rdbLinux.setText("Linux");
 
        rdbMac.setText("Mac");
 
        jLabel1.setText("Elige un sistema operativo");
 
        ckbProgramacion.setText("Programación");
 
        jLabel2.setText("Elige tu especialidad");
 
        ckbDiseno.setText("Diseño gráfico");
 
        ckbAdministracion.setText("Administración");
 
        btnGenerar.setText("Generar");
        btnGenerar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnGenerarActionPerformed(evt);
            }
        });
 
        sldHoras.setMaximum(10);
        sldHoras.setValue(0);
        sldHoras.addChangeListener(new javax.swing.event.ChangeListener() {
            public void stateChanged(javax.swing.event.ChangeEvent evt) {
                sldHorasStateChanged(evt);
            }
        });
 
        jLabel3.setText("Horas que dedicas en el ordenador");
 
        lblHoras.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        lblHoras.setText("0");
 
        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                        .addGap(22, 22, 22)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(ckbProgramacion)
                            .addComponent(jLabel2)
                            .addComponent(ckbAdministracion)
                            .addComponent(ckbDiseno)
                            .addComponent(jLabel3)
                            .addComponent(jLabel1)
                            .addComponent(rdbLinux)
                            .addComponent(rdbMac)
                            .addComponent(rdbWindows)))
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(lblHoras, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(sldHoras, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jSeparator2, javax.swing.GroupLayout.PREFERRED_SIZE, 189, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(24, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 188, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))
            .addGroup(layout.createSequentialGroup()
                .addGap(66, 66, 66)
                .addComponent(btnGenerar)
                .addGap(0, 0, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(37, 37, 37)
                .addComponent(jLabel1)
                .addGap(18, 18, 18)
                .addComponent(rdbWindows)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(rdbLinux)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(rdbMac)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 10, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel2)
                .addGap(13, 13, 13)
                .addComponent(ckbProgramacion)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(ckbDiseno)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(ckbAdministracion)
                .addGap(19, 19, 19)
                .addComponent(jSeparator2, javax.swing.GroupLayout.PREFERRED_SIZE, 11, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel3)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(sldHoras, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 1, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(lblHoras, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(18, 18, 18)
                .addComponent(btnGenerar)
                .addContainerGap(21, Short.MAX_VALUE))
        );
 
        pack();
    }// </editor-fold>                        
 
    private void btnGenerarActionPerformed(java.awt.event.ActionEvent evt) {                                           
        
        String informacion="Tu sistema operativo preferido es ";
         
        //Cogemos todos los radiobutton en un array
        JRadioButton[] rdbs={rdbWindows, rdbLinux, rdbMac};
         
        for(int i=0;i<rdbs.length;i++){
             
            //Si esta seleccionado, coge el texto
            if(rdbs[i].isSelected()){
                informacion+=rdbs[i].getText();
            }
             
        }
         
        //Hacemos igual con los checkboxes
        JCheckBox[] ckbs={ckbProgramacion, ckbDiseno, ckbAdministracion};
         
        informacion+=", \ntus especialidades son ";
         
        for(int i=0;i<ckbs.length;i++){
             
            if(ckbs[i].isSelected()){
                informacion+=ckbs[i].getText()+" "; //Ponemos un espacio por si hay mas de un elemento seleccionado
            }
             
        }
         
        informacion+=" \ny el numero de horas dedicadas al ordenador son "+sldHoras.getValue();
         
        JOptionPane.showMessageDialog(this, informacion, "Muestra de datos", JOptionPane.INFORMATION_MESSAGE);
         
    }                                          
 
    private void sldHorasStateChanged(javax.swing.event.ChangeEvent evt) {                                      
         
        lblHoras.setText(String.valueOf(sldHoras.getValue()));
         
    }                                     
 
    public static void main(String args[]) {

        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(MiniEncuestaApp.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(MiniEncuestaApp.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(MiniEncuestaApp.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(MiniEncuestaApp.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
 
        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new MiniEncuestaApp().setVisible(true);
            }
        });
    }
}