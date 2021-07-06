package semana_dos_ejercicios;

public class Potencia {
    
    //Declaracion variables de clase
    private Double b;
    private int e;
    private Double valor;
        
    //Constructor de la clase
    // private Potencia(double base, int exp){

    //     //this: referencia al objeto actual, cuyo método está siendo invocado.
    //     this.b = base;
    //     this.e = exp;
    //     this.valor = 1.0;
        
    //     if (exp >= 0){
    //         this.valor = this.valor * Math.pow(base,exp);
    //     } else{
    //          valor = 0.0;    
    //         return ;
    //     }
    // }

    // Java permite que el nombre de un parámetro/variable local sea el mismo que el nombre de una variable de instancia, en este caso, el nombre local oculta la variable de instancia.
    
    private Potencia(double b, int e){
        this.b = b;
        this.e = e;
        valor = 1.0;
        
        if (e >= 0){
            valor = valor * Math.pow(b,e);
        } else{
            valor = 0.0;
            return ;
        }
    }
    
     //Descriptor de acceso getter. Cambiar contenidos de las variables de clase
    public Double getPotencia(){
        return this.valor;
    }

    
    public static void main(String[] args) {
        Potencia nuevaPotencia = new Potencia(4.0, -5);
        System.out.println(nuevaPotencia.valor);
    }
}
