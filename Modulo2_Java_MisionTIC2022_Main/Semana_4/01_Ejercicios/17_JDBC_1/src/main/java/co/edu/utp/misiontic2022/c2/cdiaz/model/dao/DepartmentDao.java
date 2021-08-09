package co.edu.utp.misiontic2022.c2.cdiaz.model.dao;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import co.edu.utp.misiontic2022.c2.cdiaz.model.vo.Department;

public class DepartmentDao {

    private final String FILE_NAME = "departments.txt";

    public List<Department> findAll() throws IOException {
        var response = new ArrayList<Department>();
        try (var br = new BufferedReader(new FileReader(FILE_NAME))) {
            String line = br.readLine();
            while (line != null) {
                var data = line.split(";");

                var department = new Department();
                department.setId(Integer.valueOf(data[0]));
                department.setName(data[1]);
                response.add(department);

                line = br.readLine();
            }
        }
        return response;
    }

    public Department findById(Integer id) throws IOException {
        Department response = null;
        try (var br = new BufferedReader(new FileReader(FILE_NAME))) {
            String line = br.readLine();
            while (line != null) {
                var data = line.split(";");
                if (Integer.valueOf(data[0]).equals(id)) {
                    response = new Department();
                    response.setId(Integer.valueOf(data[0]));
                    response.setName(data[1]);
                    break;
                }

                line = br.readLine();
            }
        }
        return response;
    }
}
