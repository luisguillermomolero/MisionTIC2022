package semana_dos_ejercicios;

public class Triangulo extends Figura
{
    //Se definen dos atributos: "base" y "altura" (variable de clase)
    private double base;
    private double altura;

    //Constructor de la clase "Triangulo"
    public Triangulo(String color, double base, double altura){
        //Toma de la clase abstracta "Figura" (super) el (metodo) constructor "color"
        super(color);
        this.base = base;
        this.altura = altura;
    }

    //Método que fue definido en la clase abstracta "Figura"
    public double calcularArea(){
        return (base * altura) / 2;
    }
}