package co.edu.utp.misiontic2022.c2.cdiaz.view;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLException;

import co.edu.utp.misiontic2022.c2.cdiaz.controller.HumanResourcesController;
import co.edu.utp.misiontic2022.c2.cdiaz.model.vo.Department;
import co.edu.utp.misiontic2022.c2.cdiaz.model.vo.Employee;
import co.edu.utp.misiontic2022.c2.cdiaz.util.InputUtilities;

public class EmployeeMenu {

    private static final HumanResourcesController controller;
    private static final BufferedReader input;

    static {
        controller = new HumanResourcesController();
        input = new BufferedReader(new InputStreamReader(System.in));
    }

    public static void start() {
        var mainLoop = true;
        do {
            System.out.println("");
            System.out.println("==========================================");
            System.out.println(" Gestor de empleados");
            System.out.println("==========================================");
            System.out.println("1. Listar todos los empleados");
            System.out.println("2. Consultar un empleado");
            System.out.println("3. Adicionar un nuevo empleado");
            System.out.println("4. Modificar un empleado");
            System.out.println("5. Eliminar un empleado");
            System.out.println("0. Salir");
            System.out.println("==========================================");
            System.out.print("Ingrese su opción: ");
            try {
                var opcion = Integer.valueOf(input.readLine());
                switch (opcion) {
                    case 0:
                        mainLoop = false;
                        break;
                    case 1:
                        listar();
                        break;
                    case 2:
                        consultar();
                        break;
                    case 3:
                        adicionar();
                        break;
                    case 4:
                        modificar();
                        break;
                    case 5:
                        eliminar();
                        break;
                    default:
                        System.err.println("Opción no válida");
                        InputUtilities.waitForEnter(input);
                }
            } catch (NumberFormatException | IOException e) {
                System.err.println("Ha ocurrido un error: " + e.getMessage());
            }
        } while (mainLoop);
    }

    private static void eliminar() throws IOException {
        System.out.println("");
        System.out.println("==========================================");
        System.out.println(" Eliminar un empleado");
        System.out.println("==========================================");
        try {
            System.out.print("Ingresa la identificacion del empleado: ");
            var id = Integer.valueOf(input.readLine());

            var employee = controller.deleteEmployee(id);

            if (employee != null) {
                printEmployees(employee);
                System.out.println("Empleado eliminado correctamente");
            } else {
                System.out.println("\nNo se encontró el empleado en base de datos");
            }
        } catch (Exception e) {
            System.err.println("Ha ocurrido un error: " + e.getMessage());
        }
        InputUtilities.waitForEnter(input);
    }

    private static void modificar() throws IOException {
        System.out.println("");
        System.out.println("==========================================");
        System.out.println(" Modificar un empleado");
        System.out.println("==========================================");
        try {
            System.out.print("Ingresa la identificacion del empleado: ");
            var id = Integer.valueOf(input.readLine());

            var employee = controller.findEmployee(id);

            if (employee != null) {
                printEmployees(employee);

                String name = InputUtilities.inputValidString(input, "Ingresa el nombre: ", employee.getName());
                String email = InputUtilities.inputValidString(input, "Ingresa el correo electrónico: ", employee.getEmail());

                printAllDepartments();
                var departmentId = InputUtilities.inputValidInteger(input, "Ingresa el código del departamento: ", employee.getDepartment().getId());

                employee = controller.updateEmployee(id, name, email, departmentId);
                if (employee != null) {
                    printEmployees(employee);
                    System.out.println("Empleado modificado correctamente");
                } else {
                    System.out.println("\nNo se encontró el empleado en base de datos");
                }
            } else {
                System.out.println("\nNo se encontró el empleado en base de datos");
            }
        } catch (Exception e) {
            System.err.println("Ha ocurrido un error: " + e.getMessage());
        }
        InputUtilities.waitForEnter(input);
    }

    private static void adicionar() throws IOException {
        System.out.println("");
        System.out.println("==========================================");
        System.out.println(" Adicionar un empleado");
        System.out.println("==========================================");
        try {
            var name = InputUtilities.inputValidString(input, "Ingresa el nombre: ");
            var email = InputUtilities.inputValidString(input, "Ingresa el correo electrónico: ");

            // Imprimo los departamentos
            printAllDepartments();
            var departmentId = InputUtilities.inputValidInteger(input, "Ingresa el código del departamento: ");

            var employee = controller.createEmployee(name, email, departmentId);

            if (employee != null) {
                printEmployees(employee);
                System.out.println("Empleado creado correctamente");
            } else {
                System.out.println("\nNo se encontró el empleado en base de datos");
            }
        } catch (Exception e) {
            System.err.println("Ha ocurrido un error: " + e.getMessage());
        }
        InputUtilities.waitForEnter(input);
    }

    private static void consultar() throws IOException {
        System.out.println("");
        System.out.println("==========================================");
        System.out.println(" Consultar un empleado");
        System.out.println("==========================================");
        try {
            System.out.print("Ingresa la identificacion del empleado: ");
            var id = Integer.valueOf(input.readLine());

            var employee = controller.findEmployee(id);

            if (employee != null) {
                printEmployees(employee);
            } else {
                System.out.println("\nNo se encontró el empleado en base de datos");
            }
        } catch (SQLException | NumberFormatException | IOException e) {
            System.err.println("Ha ocurrido un error: " + e.getMessage());
        }
        InputUtilities.waitForEnter(input);
    }

    private static void listar() throws IOException {
        System.out.println("");
        System.out.println("==========================================");
        System.out.println(" Listar empleados");
        System.out.println("==========================================");
        try {
            var employees = controller.findAllEmployees();

            if (employees.size() > 0) {
                printEmployees(employees.toArray(new Employee[0]));
                System.out.println(employees.size() + " empleados en Base de datos");
            } else {
                System.out.println("\nNo hay empleados en base de datos");
            }
        } catch (SQLException e) {
            System.err.println("Ha ocurrido un error: " + e.getMessage());
        }
        InputUtilities.waitForEnter(input);
    }

    private static void printAllDepartments() {
        System.out.println();
        System.out.println(" Listado departamentos");
        System.out.println("==========================================");
        System.out.println("ID\tNOMBRE");
        try {
            var departments = controller.findAllDepartments();
            for (Department department : departments) {
                System.out.printf("%d\t%s %n", department.getId(), department.getName());
            }
        } catch (SQLException e) {
            System.err.println("Ha ocurrido un error: " + e.getMessage());
        }
    }

    private static void printEmployees(Employee... employees) {
        System.out.println();
        System.out.println("ID\tNOMBRE\tEMAIL\tDEPARTAMENTO");
        for (Employee employee : employees) {
            System.out.printf("%d\t%s\t%s\t%s %n", employee.getId(), employee.getName(), employee.getEmail(),
                    employee.getDepartment().getName());
        }
    }

}
