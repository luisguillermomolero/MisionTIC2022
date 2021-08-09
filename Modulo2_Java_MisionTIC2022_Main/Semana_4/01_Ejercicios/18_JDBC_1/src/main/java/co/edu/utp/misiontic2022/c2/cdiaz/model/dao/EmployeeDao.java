package co.edu.utp.misiontic2022.c2.cdiaz.model.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import co.edu.utp.misiontic2022.c2.cdiaz.model.vo.Employee;
import co.edu.utp.misiontic2022.c2.cdiaz.util.JDBCUtilities;

public class EmployeeDao {

    private DepartmentDao departmentDao;

    public EmployeeDao() {
        departmentDao = new DepartmentDao();
    }

    public List<Employee> findAll() throws SQLException {
        var response = new ArrayList<Employee>();
        Connection connection = null;
        try {
            connection = JDBCUtilities.getConnection();
            var statement = connection.prepareStatement("select * from employees");
            var rset = statement.executeQuery();
            while (rset.next()) {
                var employee = new Employee();
                employee.setId(rset.getInt(1));
                employee.setName(rset.getString(2));
                employee.setEmail(rset.getString(3));
                employee.setDepartment(departmentDao.findById(rset.getInt(4)));
                response.add(employee);
            }
            rset.close();
            statement.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
        return response;
    }

    public Employee findById(Integer id) throws SQLException {
        Employee response = null;
        Connection connection = null;
        try {
            connection = JDBCUtilities.getConnection();
            var statement = connection.prepareStatement("select * from employees where id = ?");
            statement.setInt(1, id);

            var rset = statement.executeQuery();
            if (rset.next()) {
                response = new Employee();
                response.setId(rset.getInt(1));
                response.setName(rset.getString(2));
                response.setEmail(rset.getString(3));
                response.setDepartment(departmentDao.findById(rset.getInt(4)));
            }
            rset.close();
            statement.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
        return response;
    }

    public Employee save(Employee employee) throws SQLException {
        Connection connection = null;
        PreparedStatement statement = null; 
        try {
            connection = JDBCUtilities.getConnection();
            if (employee.getId() == null) {
                employee.setId(generarConsecutivo());
                
                statement = connection.prepareStatement("insert into employees values (?, ?, ?, ?)");
                statement.setInt(1, employee.getId());
                statement.setString(2, employee.getName());
                statement.setString(3, employee.getEmail());
                statement.setInt(4, employee.getDepartment().getId());

                statement.executeUpdate();
            } else {
                
                statement = connection
                        .prepareStatement("update employees set name = ?, email = ?, department_id = ? where id = ?");
                statement.setString(1, employee.getName());
                statement.setString(2, employee.getEmail());
                statement.setInt(3, employee.getDepartment().getId());
                statement.setInt(4, employee.getId());

                statement.executeUpdate();
            }
            statement.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
        return employee;
    }

    public Employee delete(Integer id) throws SQLException, Exception {
        Connection connection = null;
        var employee = findById(id);
        if (employee == null) {
            throw new Exception("Empleado no existe");
        }

        try {
            connection = JDBCUtilities.getConnection();
            var statement = connection.prepareStatement("delete from employees where id = ?");
            statement.setInt(1, id);
            statement.executeUpdate();
            statement.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
        return employee;
    }

    private Integer generarConsecutivo() throws SQLException {
        Integer consecutivo = 1;
        Connection connection = null;
        try {
            connection = JDBCUtilities.getConnection();
            var statement = connection.prepareStatement("select max(id) as consecutivo from employees");
            var rset = statement.executeQuery();
            if (rset.next()) {
                consecutivo = rset.getInt("consecutivo") + 1;
            }
            rset.close();
            statement.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
        return consecutivo;
    }

}
