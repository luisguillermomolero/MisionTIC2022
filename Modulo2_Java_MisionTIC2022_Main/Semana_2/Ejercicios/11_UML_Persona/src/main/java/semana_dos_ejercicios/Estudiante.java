package semana_dos_ejercicios;

public class Estudiante extends Persona{

    private String carrera; 
    private int legajo;

    public Estudiante(){ 
    }

    public String getCarrera(){
        return carrera;
    }
    public void setCarrera(String val){
        this.carrera = val;
    }
    public int getLegajo(){
        return legajo;
    }
    public void setLegajo(int val){
        this.legajo = val;
    }
}
