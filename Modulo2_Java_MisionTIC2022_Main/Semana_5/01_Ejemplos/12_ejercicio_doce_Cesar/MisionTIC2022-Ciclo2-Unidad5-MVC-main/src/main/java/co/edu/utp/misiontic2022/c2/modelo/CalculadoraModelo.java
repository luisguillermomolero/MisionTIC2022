package co.edu.utp.misiontic2022.c2.modelo;

public class CalculadoraModelo {

    private Integer numeroUno;
    private Integer numeroDos;
    private Integer resultado;

    public Integer getNumeroUno() {
        return numeroUno;
    }

    public void setNumeroUno(Integer numeroUno) {
        this.numeroUno = numeroUno;
    }

    public Integer getNumeroDos() {
        return numeroDos;
    }

    public void setNumeroDos(Integer numeroDos) {
        this.numeroDos = numeroDos;
    }

    public Integer getResultado() {
        return resultado;
    }

    public void setResultado(Integer resultado) {
        this.resultado = resultado;
    }

    public Integer sumar() {
        resultado = numeroUno + numeroDos;
        return resultado;
    }

    public Integer restar() {
        resultado = numeroUno - numeroDos;
        return resultado;
    }

    public Integer multiplicar() {
        resultado = numeroUno * numeroDos;
        return resultado;
    }

    public Integer dividir() {
        resultado = numeroUno / numeroDos;
        return resultado;
    }

    public Integer calcularModulo() {
        resultado = numeroUno % numeroDos;
        return resultado;
    }

}
