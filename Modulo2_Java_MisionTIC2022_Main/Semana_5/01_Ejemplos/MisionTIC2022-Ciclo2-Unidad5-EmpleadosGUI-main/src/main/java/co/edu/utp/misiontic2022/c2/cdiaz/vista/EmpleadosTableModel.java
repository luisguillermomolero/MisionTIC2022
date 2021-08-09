/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package co.edu.utp.misiontic2022.c2.cdiaz.vista;

import co.edu.utp.misiontic2022.c2.cdiaz.modelo.vo.Employee;
import java.util.List;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author ROG
 */
public class EmpleadosTableModel extends AbstractTableModel {
    
    private final List<Employee> employees;

    public EmpleadosTableModel(List<Employee> employees) {
        this.employees = employees;        
    }
    
    public void addEmployee(Employee employee){
        employees.add(employee);
        fireTableDataChanged();
    }
    
    public void setEmployee(int row, Employee employee){
        employees.set(row, employee);
        fireTableDataChanged();
    }
    
    public void removeEmployee(int row) {
        employees.remove(row);
        fireTableDataChanged();
    }
    
    public Employee getEmployee(int row) {
        return employees.get(row);
    }

    @Override
    public String getColumnName(int column) {
        switch (column) {
            case 0:
                return "ID";
            case 1:
                return "Nombre";
            case 2:
                return "Departamento";
            default:
                throw new AssertionError();
        }
    }

    @Override
    public int getRowCount() {
        return employees.size();
    }

    @Override
    public int getColumnCount() {
        return 3;
    }

    @Override
    public Object getValueAt(int row, int column) {
        var employee = employees.get(row);
        switch (column) {
            case 0:
                return employee.getId();
            case 1:
                return employee.getName();
            case 2:
                return employee.getDepartment().getName();
            default:
                throw new AssertionError();
        }
    }

}
