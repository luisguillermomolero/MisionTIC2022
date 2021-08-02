package co.edu.utp.misiontic2022.c2.cdiaz.modelo.dao;

import co.edu.utp.misiontic2022.c2.cdiaz.modelo.vo.Employee;
import java.util.List;

import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;


public class EmployeeDao {

    private final EntityManagerFactory emf;

    public EmployeeDao() {
        emf = Persistence.createEntityManagerFactory("employees-pu");
    }

    public List<Employee> findAll() {
        List<Employee> employees = null;
        var em = emf.createEntityManager();
        try {
            //JPQL - Java Persistence Query Language
            var query = em.createQuery("SELECT e FROM Employee e", Employee.class);
            employees = query.getResultList();
        } finally {
            em.close();
        }
        return employees;
    }

    public Employee findById(Integer id) {
        Employee response = null;

        var em = emf.createEntityManager();
        try {
            response = em.find(Employee.class, id);
        } finally {
            em.close();
        }
        return response;
    }

    public Employee save(Employee employee) {
        var em = emf.createEntityManager();
        try {
            if (employee.getId() != null){
                // Para actualizar un registro, es necesario enviar
                // un dato enlazado (attached) a la base de datos
                var actual = em.find(Employee.class, employee.getId());
                actual.setName(employee.getName());
                actual.setEmail(employee.getEmail());
                actual.setDepartment(employee.getDepartment());

                employee = actual;
            }
            em.getTransaction().begin();
            em.persist(employee);
            em.getTransaction().commit();
        } finally {
            em.close();
        }
        return employee;
    }

    public Employee delete(Integer id) throws Exception {
        Employee employee = null;
        var em = emf.createEntityManager();
        try {
            employee = em.find(Employee.class, id);
            if (employee == null) {
                throw new Exception("Empleado no existe");
            }
            em.getTransaction().begin();
            em.remove(employee);
            em.getTransaction().commit();
        } finally {
            em.close();
        }
        return employee;
    }

}
