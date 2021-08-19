import java.awt.EventQueue;

import view.VistaRequerimientosReto4;

public class App {
    public static void main( String[] args ){        
        
        // Ejecutar Swing en otro hilo
        EventQueue.invokeLater(new Runnable(){
            @Override
            public void run() {
                try{
                    VistaRequerimientosReto4 frame = new VistaRequerimientosReto4();
                    frame.setVisible(true);
                } catch(Exception e){
                    e.printStackTrace();
                }
                
            }
            
        });
        
    }

}
