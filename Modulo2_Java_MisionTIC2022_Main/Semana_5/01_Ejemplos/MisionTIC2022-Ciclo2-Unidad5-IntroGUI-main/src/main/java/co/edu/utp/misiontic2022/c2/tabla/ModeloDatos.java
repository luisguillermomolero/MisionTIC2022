package co.edu.utp.misiontic2022.c2.tabla;

import javax.swing.table.AbstractTableModel;

public class ModeloDatos extends AbstractTableModel {

    Object datos[][] = { 
            { "uno", "dos", "tres", "cuatro" }, 
            { "cinco", "seis", "siete", "ocho" },
            { "nueve", "diez", "once", "doce" } };

    public ModeloDatos() {
        addTableModelListener(evt -> {
            for (int i = 0; i < datos.length; i++) {
                for (int j = 0; j < datos[0].length; j++) {
                    System.out.print(datos[i][j] + " ");
                }
                System.out.println();
            }
        });
    }

    @Override
    public int getRowCount() {
        return datos.length;
    }

    @Override
    public int getColumnCount() {
        return datos[0].length;
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        return datos[rowIndex][columnIndex];
    }

    @Override
    public void setValueAt(Object aValue, int rowIndex, int columnIndex) {
        datos[rowIndex][columnIndex] = aValue;
        fireTableDataChanged();
    }

    @Override
    public boolean isCellEditable(int rowIndex, int columnIndex) {
        return true;
    }

}
