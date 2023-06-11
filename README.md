# Simulacion-Sistemas-Continuos

Ejercicio 6 del practico de sistemas continuos, Simulación, UNRC, 2023.

Lenguaje: Python 3

Dependencias Usadas:  

            - Matplotlib
            - Pandas
            - Decimal
            - sys

si falta alguna dependencia ejecutar la siguiente linea en la terminal:

```
pip3 install -r requirements.txt
```


Modo de uso: Ejecutar el archivo Ejercicio6-Bortol-Fungo.py con python3 el cual generar un archivo csv con el siguiente formato, data_NUMERODET_tries.csv, 
donde NUMERODET es el t maximo el cual se puede modificar dentro del programa, 
junto con la altura min para alcanzar, el paso con el que se calcula  y la altura del cual empieza, luego hay 2 opciones:
  
- Para 1 solo archivo de datos generado: ejecutar el archivo Plotter.py data_NUMERODET_tries.csv, el cual generara un archivo png con el grafico de la simulacion. 
Por Ejemplo:
```
python3 Plotter.py data_100_tries.csv
```
- Para todos los archivos de datos generados: Hay un script que se llama PlottearTodosLosGraficos que ejecuta cada instancia creada de data_NUMERODET_tries.csv


Autores:
- Juan Pablo Bortol
- Augusto Fungo
        
