package co.edu.utp.misiontic2022.c2.cdiaz.controller;

import java.sql.SQLException;
import java.util.List;

import co.edu.utp.misiontic2022.c2.cdiaz.model.dao.DepartmentDao;
import co.edu.utp.misiontic2022.c2.cdiaz.model.dao.EmployeeDao;
import co.edu.utp.misiontic2022.c2.cdiaz.model.vo.Department;
import co.edu.utp.misiontic2022.c2.cdiaz.model.vo.Employee;

public class HumanResourcesController {

    private final DepartmentDao departmentDao;
    private final EmployeeDao employeeDao;

    public HumanResourcesController() {
        this.departmentDao = new DepartmentDao();
        this.employeeDao = new EmployeeDao();
    }

    public List<Department> findAllDepartments() throws SQLException {
        return departmentDao.findAll();
    }

    public List<Employee> findAllEmployees() throws SQLException {
        return employeeDao.findAll();
    }

    public Employee findEmployee(Integer id) throws SQLException {
        return employeeDao.findById(id);
    }

    public Employee createEmployee(String name, String email, Integer departmentId) throws SQLException {
        var employee = new Employee();
        employee.setName(name);
        employee.setEmail(email);
        employee.setDepartment(departmentDao.findById(departmentId));

        employee = employeeDao.save(employee);

        return employee;
    }

    public Employee updateEmployee(Integer id, String name, String email, Integer departmentId) throws SQLException {
        var employee = new Employee();
        employee.setId(id);
        employee.setName(name);
        employee.setEmail(email);
        employee.setDepartment(departmentDao.findById(departmentId));

        employee = employeeDao.save(employee);

        return employee;
    }
    public Employee deleteEmployee(Integer id) throws Exception {
        return employeeDao.delete(id);
    }

}
