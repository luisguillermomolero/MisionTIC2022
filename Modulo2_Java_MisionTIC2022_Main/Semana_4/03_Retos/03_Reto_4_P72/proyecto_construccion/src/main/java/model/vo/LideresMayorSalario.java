package model.vo;

public class LideresMayorSalario {

    private Integer idLider;
    private String nombre;
    private String primerApellido;
    private Integer salario;
    private String ciudadNacimiento;

    public LideresMayorSalario() {
    }

    public LideresMayorSalario(Integer idLider, String nombre, String primerApellido, Integer salario, String ciudadNacimiento) {
        this.idLider = idLider;
        this.nombre = nombre;
        this.primerApellido = primerApellido;
        this.salario = salario;
        this.ciudadNacimiento = ciudadNacimiento;
    }

    public Integer getIdLider() {
        return idLider;
    }

    public void setIdLider(Integer idLider) {
        this.idLider = idLider;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getPrimerApellido() {
        return primerApellido;
    }

    public void setPrimerApellido(String primerApellido) {
        this.primerApellido = primerApellido;
    }

    public Integer getSalario() {
        return salario;
    }

    public void setSalario(Integer salario) {
        this.salario = salario;
    }

    public String getCiudadNacimiento() {
        return ciudadNacimiento;
    }

    public void setCiudadNacimiento(String ciudadNacimiento) {
        this.ciudadNacimiento = ciudadNacimiento;
    }

    }
