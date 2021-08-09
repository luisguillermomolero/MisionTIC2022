package co.edu.utp.misiontic2022.c2.cdiaz.model.dao;

import java.util.List;

import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import co.edu.utp.misiontic2022.c2.cdiaz.model.vo.Employee;

public class EmployeeDao {

    private final EntityManagerFactory emf;

    public EmployeeDao() {
        emf = Persistence.createEntityManagerFactory("employees-pu");
    }

    public List<Employee> findAll() {
        List<Employee> employees = null;
        var em = emf.createEntityManager();
        try {
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
            em.getTransaction().begin(); // Iniciar transacción
            em.persist(employee); //persiste el objeto empleado.Cambio/estado
            em.getTransaction().commit(); //Actualizar cambios en bd
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
