package co.edu.utp.misiontic2022.c2.vista;

import co.edu.utp.misiontic2022.c2.controlador.CalculadoraController;

public interface CalculadoraVista {

    public String getNumeroUno();

    public String getNumeroDos();

    public void setResultado(String resultado);

    public void iniciar(CalculadoraController controller);

    public void mostrarExcepcion(Exception ex);

}
