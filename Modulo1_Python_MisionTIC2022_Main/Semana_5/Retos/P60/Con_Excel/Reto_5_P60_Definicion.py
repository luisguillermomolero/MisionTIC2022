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
        #Se lee e importa un subconjunto de columnas desde la 'A' hasta la 'G' (Indice+2)
        subconjuntoColumnas = pd.read_excel(rutaFileXls, usecols = 'A:G')
        subconjuntoColumnas.head()
        #print('Subconjunto\n')
        #print(subconjuntoColumnas) #Se muestra el subconjunto de películas [1338 rows x 2 columns]
        """
        En el archivo de Excel, teniendo las columnas "Gross Earnings" y "Budget"
        se resta el presupuesto de las ganancias brutas para obtener las "Net Earnings". 
        Luego se aplica esta fórmula en el archivo de Excel a todas las filas.
        """
        peliculas["Net Earnings"] = peliculas["Gross Earnings"] - peliculas["Budget"]
        """
        Con "sot_values" se ordenan los datos por la columna "Net Earnings"
        Se muestran los 10 primeros registros de películas principales por "Net Earnings"
        """
        ordenarPeliculas = peliculas[['Net Earnings']].sort_values(['Net Earnings'], ascending=[False])
        ordenarPeliculas.head(10)['Net Earnings'].plot(kind="pie")
        #Se importa la libreria matplotlib.pyplot
        #import matplotlib.pyplot as plt
        #Se muestra la columna 'Net Earnings' ordenada [5042 rows x 1 columns]
        print(ordenarPeliculas)
        #Se muestra el resultado con un diagrama tipo pie de los primeros 10 registros.
        #plt.show()
    
    else:
        print('Extensión inválida.')
    return 'Fin del registro'
print(listaPeliculas(rutaFileXls))