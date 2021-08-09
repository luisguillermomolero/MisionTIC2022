package semana_dos_ejercicios;

public class Cuadrado extends Figura
{
    //Se define un atributo: "lado"  (variable de clase)
    private double lado;

    //Constructor de la clase "Cuadrado"
    public Cuadrado(String color, double lado){
        //Toma de la clase abstracta "Figura" (super) el (metodo) constructor "color"
        super(color);
        this.lado = lado;
    }

    //Método que fue definido en la clase abstracta "Figura"
    public double calcularArea(){
        return lado * lado;
    }
}