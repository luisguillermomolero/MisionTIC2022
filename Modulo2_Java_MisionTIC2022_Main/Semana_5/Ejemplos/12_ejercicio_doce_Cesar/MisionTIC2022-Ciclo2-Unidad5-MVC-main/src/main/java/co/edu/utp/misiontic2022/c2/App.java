package co.edu.utp.misiontic2022.c2;

import co.edu.utp.misiontic2022.c2.controlador.CalculadoraController;
import co.edu.utp.misiontic2022.c2.modelo.CalculadoraModelo;
import co.edu.utp.misiontic2022.c2.vista.CalculadoraConsola;
import co.edu.utp.misiontic2022.c2.vista.CalculadoraRestaGUI;
import co.edu.utp.misiontic2022.c2.vista.CalculadoraSumaGUI;
import co.edu.utp.misiontic2022.c2.vista.CalculadoraVista;

/**
 * Hello world!
 *
 */
public class App {
    private enum TipoVista {
        CONSOLA, SUMA_GUI, RESTA_GUI, MULTIPLICACION_GUI, DIVISION_GUI, MODULO_GUI
    }

    public static void main(String[] args) {
        var tipo = TipoVista.CONSOLA;

        CalculadoraVista view = null;
        switch (tipo) {
            case CONSOLA:
                view = new CalculadoraConsola();
                break;
            case SUMA_GUI:
                view = new CalculadoraSumaGUI();
                break;
            case RESTA_GUI:
                view = new CalculadoraRestaGUI();
                break;
            case MULTIPLICACION_GUI:
                // TODO: Implementar una vista para la multiplicación
                throw new UnsupportedOperationException("Implementar una vista para la multiplicación");
            case DIVISION_GUI:
                // TODO: Implementar una vista para la división
                throw new UnsupportedOperationException("Implementar una vista para la división");
            case MODULO_GUI:
                // TODO: Implementar una vista para el módulo (resto de división)
                throw new UnsupportedOperationException("Implementar una vista para el módulo (resto de división)");
            default:
                return;
        }

        var model = new CalculadoraModelo();
        var controller = new CalculadoraController(view, model);

        controller.iniciar();
    }
}
