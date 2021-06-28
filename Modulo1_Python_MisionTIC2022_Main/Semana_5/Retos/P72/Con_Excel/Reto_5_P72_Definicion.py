#importando el módulo pandas.
import pandas as pd

"""
Se leen los datos de un archivo Excel en un objeto Panda DataFrame. 
Asimismo, pandas almacena datos de forma predeterminada en el DataFrame. 
Luego se almacena este DataFrame en una variable llamada peliculas.
"""

rutaFileXls = 'https://github.com/luisguillermomolero/MisionTIC2022/blob/ff05b5f12ea60cf2f005309f011c1d48ab4725cb/movies.xls?raw=true'
#rutaFileXls = 'movies.xls' #ruta de la base de datos

def listaPeliculas(rutaFileXls: str)-> str:
    #if rutaFileXls.endswith('.xls'): #Condicion de entrada (True) si la cadena termina con el sufijo ".xls"
    #if not rutaFileXls.endswith('.xls'): #Condicion de entrada (True) si la cadena termina con el sufijo ".xls"
    if rutaFileXls.split('.')[-1] != 'xls': #Condicion de entrada (True) si la cadena termina con el sufijo ".xls"
        try:
            xlsx = pd.ExcelFile(rutaFileXls)    #Importar Bd Excel "movies.xls"
            registroPeliculas = []              #Inicializa la lista
            for hojas in xlsx.sheet_names:      #Concatenar todas las hojas de excel en un sola lista
                registroPeliculas.append(xlsx.parse(hojas)) 
            peliculas = pd.concat(registroPeliculas)    #Concatena todas las hojas de la bd excel en "registroPeliculas"
        except: 
            print('Error al leer el archivo de datos.')
        #Se selecciona la columna 'Year' como indice y la columna 'Gross Earnings' para aplicar la fórmula de resumen
        subGrupoPeliculas = peliculas[['Year', 'Gross Earnings']]
        subGrupoPeliculas.head()
        #Con pivot_table indexamos 'Year'
        gananciaAno = subGrupoPeliculas.pivot_table(index=['Year'])
        gananciaAno.head()
        #Se importa la libreria matplotlib.pyplot
        import matplotlib.pyplot as plt
        gananciaAno.plot()
        #Se muestra la columna 'Net Earnings' [76 rows x 1 columns]
        print(gananciaAno)
        #print('\n Ganancia por Año')
        #Se muestra el resultado con la grafica
        #plt.show()

    
    else:
        print('Extensión inválida.')
    return 'Fin del registro'
print(listaPeliculas(rutaFileXls))