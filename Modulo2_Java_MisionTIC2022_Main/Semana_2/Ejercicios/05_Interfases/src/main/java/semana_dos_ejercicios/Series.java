package semana_dos_ejercicios;

/**Interfases
 * Define métodos sin cuerpo
 * Implementados por subclases
 * 
 * <(modificador)"public" o "default"> interface <nombre>(<tipo parametro>)
 * 
 * Donde 
 *      public: para todos los paquetes
 *      default: No se coloca y solo es vista desde otros miembors del mismo paquete
 * 
 * Las variables declaradas en una interfaz no son variables de instancia. En cambio, son implícitamente public, final, y static, y deben inicializarse. Por lo tanto, son esencialmente constantes.
 * 
 * 
 */
public interface Series {
    int getSiguiente(); //Retorna el siguiente número de la serie
    void reiniciar(); //Reinicia
    void setComenzar(int x); //Establece un valor inicial
}