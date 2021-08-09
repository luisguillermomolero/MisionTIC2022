package co.edu.utp.misiontic2022.c2.cdiaz.model.dao;

import java.util.List;

import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import co.edu.utp.misiontic2022.c2.cdiaz.model.vo.Department;

public class DepartmentDao {

    private final EntityManagerFactory emf;

    public DepartmentDao() {
        emf = Persistence.createEntityManagerFactory("employees-pu");
    }

    public List<Department> findAll() {
        List<Department> employees = null;
        var em = emf.createEntityManager();
        try {
            var query = em.createQuery("SELECT d FROM Department d", Department.class);
            employees = query.getResultList();
        } finally {
            em.close();
        }
        return employees;
    }

    public Department findById(Integer id) {
        Department response = null;

        var em = emf.createEntityManager();
        try {
            response = em.find(Department.class, id);
        } finally {
            em.close();
        }
        return response;
    }
}
