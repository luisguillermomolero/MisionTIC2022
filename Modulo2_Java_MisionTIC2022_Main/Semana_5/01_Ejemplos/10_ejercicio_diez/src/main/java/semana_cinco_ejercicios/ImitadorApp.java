//App imitador

package semana_cinco_ejercicios;

import javax.swing.ButtonGroup;
 
public class ImitadorApp extends javax.swing.JFrame {

    private javax.swing.JCheckBox ckb1Imitacion;
    private javax.swing.JCheckBox ckb1Original;
    private javax.swing.JCheckBox ckb2Imitacion;
    private javax.swing.JCheckBox ckb2Original;
    private javax.swing.JCheckBox ckb3Imitacion;
    private javax.swing.JCheckBox ckb3Original;
    private javax.swing.JComboBox cmbImitacion;
    private javax.swing.JComboBox cmbOriginal;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JRadioButton rdb1Imitacion;
    private javax.swing.JRadioButton rdb1Original;
    private javax.swing.JRadioButton rdb2Imitacion;
    private javax.swing.JRadioButton rdb2Original;
    private javax.swing.JRadioButton rdb3Imitacion;
    private javax.swing.JRadioButton rdb3Original;
    private javax.swing.JSpinner spnImitacion;
    private javax.swing.JSpinner spnOriginal;
    private javax.swing.JTextField txtImitacion;
    private javax.swing.JTextField txtOriginal;

 
    public ImitadorApp() {
        initComponents();
     
        //añadimos los radiobutton en sus respectivos grupos
        ButtonGroup btg1=new ButtonGroup();
         
        btg1.add(rdb1Original);
        btg1.add(rdb2Original);
        btg1.add(rdb3Original);
         
        ButtonGroup btg2=new ButtonGroup();
         
        btg2.add(rdb1Imitacion);
        btg2.add(rdb2Imitacion);
        btg2.add(rdb3Imitacion);
         
    }
 
    private void initComponents() {
 
        jSeparator1 = new javax.swing.JSeparator();
        spnOriginal = new javax.swing.JSpinner();
        rdb3Original = new javax.swing.JRadioButton();
        ckb1Original = new javax.swing.JCheckBox();
        ckb2Original = new javax.swing.JCheckBox();
        rdb1Original = new javax.swing.JRadioButton();
        ckb3Original = new javax.swing.JCheckBox();
        rdb2Original = new javax.swing.JRadioButton();
        cmbOriginal = new javax.swing.JComboBox();
        txtOriginal = new javax.swing.JTextField();
        txtImitacion = new javax.swing.JTextField();
        spnImitacion = new javax.swing.JSpinner();
        cmbImitacion = new javax.swing.JComboBox();
        rdb3Imitacion = new javax.swing.JRadioButton();
        ckb1Imitacion = new javax.swing.JCheckBox();
        ckb2Imitacion = new javax.swing.JCheckBox();
        rdb1Imitacion = new javax.swing.JRadioButton();
        ckb3Imitacion = new javax.swing.JCheckBox();
        rdb2Imitacion = new javax.swing.JRadioButton();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
 
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Imitador");
 
        spnOriginal.addChangeListener(new javax.swing.event.ChangeListener() {
            public void stateChanged(javax.swing.event.ChangeEvent evt) {
                spnOriginalStateChanged(evt);
            }
        });
 
        rdb3Original.setText("Opcion 3");
        rdb3Original.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                rdb3OriginalActionPerformed(evt);
            }
        });
 
        ckb1Original.setText("Opcion 4");
        ckb1Original.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ckb1OriginalActionPerformed(evt);
            }
        });
 
        ckb2Original.setText("Opcion 5");
        ckb2Original.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ckb2OriginalActionPerformed(evt);
            }
        });
 
        rdb1Original.setText("Opcion 1");
        rdb1Original.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                rdb1OriginalActionPerformed(evt);
            }
        });
 
        ckb3Original.setText("Opcion 6");
        ckb3Original.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ckb3OriginalActionPerformed(evt);
            }
        });
 
        rdb2Original.setText("Opcion 2");
        rdb2Original.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                rdb2OriginalActionPerformed(evt);
            }
        });
 
        cmbOriginal.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));
        cmbOriginal.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                cmbOriginalItemStateChanged(evt);
            }
        });
 
        txtOriginal.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtOriginalKeyTyped(evt);
            }
        });
 
        txtImitacion.setEnabled(false);
 
        spnImitacion.setEnabled(false);
 
        cmbImitacion.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));
        cmbImitacion.setEnabled(false);
 
        rdb3Imitacion.setText("Opcion 3");
        rdb3Imitacion.setEnabled(false);
 
        ckb1Imitacion.setText("Opcion 4");
        ckb1Imitacion.setEnabled(false);
 
        ckb2Imitacion.setText("Opcion 5");
        ckb2Imitacion.setEnabled(false);
 
        rdb1Imitacion.setText("Opcion 1");
        rdb1Imitacion.setEnabled(false);
 
        ckb3Imitacion.setText("Opcion 6");
        ckb3Imitacion.setEnabled(false);
 
        rdb2Imitacion.setText("Opcion 2");
        rdb2Imitacion.setEnabled(false);
 
        jLabel1.setText("Original");
 
        jLabel2.setText("Espejo");
 
        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jSeparator1)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(23, 23, 23)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(rdb2Original)
                            .addComponent(rdb1Original)
                            .addComponent(rdb3Original))
                        .addGap(26, 26, 26)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(ckb2Original)
                            .addComponent(ckb1Original)
                            .addComponent(ckb3Original))
                        .addGap(30, 30, 30)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(txtOriginal)
                            .addComponent(cmbOriginal, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(spnOriginal, javax.swing.GroupLayout.PREFERRED_SIZE, 105, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(20, 20, 20)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(rdb2Imitacion)
                            .addComponent(rdb1Imitacion)
                            .addComponent(rdb3Imitacion))
                        .addGap(26, 26, 26)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(ckb2Imitacion)
                            .addComponent(ckb1Imitacion)
                            .addComponent(ckb3Imitacion))
                        .addGap(37, 37, 37)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(txtImitacion)
                            .addComponent(cmbImitacion, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(spnImitacion, javax.swing.GroupLayout.PREFERRED_SIZE, 105, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(jLabel1))
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(jLabel2)))
                .addContainerGap(26, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(27, 27, 27)
                                .addComponent(ckb1Original))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addContainerGap()
                                .addComponent(jLabel1)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(rdb1Original)))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(rdb2Original)
                            .addComponent(ckb2Original))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 9, Short.MAX_VALUE)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(ckb3Original)
                            .addComponent(rdb3Original))
                        .addGap(41, 41, 41))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(27, 27, 27)
                        .addComponent(txtOriginal, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(cmbOriginal, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(spnOriginal, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
                .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 10, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel2)
                .addGap(5, 5, 5)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(rdb1Imitacion)
                            .addComponent(ckb1Imitacion))
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(txtImitacion, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(cmbImitacion, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                .addComponent(rdb2Imitacion)
                                .addComponent(ckb2Imitacion)))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(spnImitacion, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(ckb3Imitacion)
                            .addComponent(rdb3Imitacion))
                        .addGap(0, 39, Short.MAX_VALUE))))
        );
 
        pack();
    }// </editor-fold>                        
 
    private void rdb1OriginalActionPerformed(java.awt.event.ActionEvent evt) {                                             
         
        rdb1Imitacion.setSelected(true);
         
    }                                            
 
    private void rdb2OriginalActionPerformed(java.awt.event.ActionEvent evt) {                                             
        rdb2Imitacion.setSelected(true);
    }                                            
 
    private void rdb3OriginalActionPerformed(java.awt.event.ActionEvent evt) {                                             
        rdb3Imitacion.setSelected(true);
    }                                            
 
    private void ckb1OriginalActionPerformed(java.awt.event.ActionEvent evt) {                                             
        ckb1Imitacion.setSelected(ckb1Original.isSelected());
    }                                            
 
    private void ckb2OriginalActionPerformed(java.awt.event.ActionEvent evt) {                                             
        ckb2Imitacion.setSelected(ckb2Original.isSelected());
    }                                            
 
    private void ckb3OriginalActionPerformed(java.awt.event.ActionEvent evt) {                                             
        ckb3Imitacion.setSelected(ckb3Original.isSelected());
    }                                            
 
    private void txtOriginalKeyTyped(java.awt.event.KeyEvent evt) {                                     
        txtImitacion.setText(txtOriginal.getText());
    }                                    
 
    private void spnOriginalStateChanged(javax.swing.event.ChangeEvent evt) {                                         
        spnImitacion.setValue((Integer)spnOriginal.getValue());
    }                                        
 
    private void cmbOriginalItemStateChanged(java.awt.event.ItemEvent evt) {                                             
        cmbImitacion.setSelectedIndex(cmbOriginal.getSelectedIndex());
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
            java.util.logging.Logger.getLogger(ImitadorApp.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(ImitadorApp.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(ImitadorApp.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ImitadorApp.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
 
        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new ImitadorApp().setVisible(true);
            }
        });
    }
}
