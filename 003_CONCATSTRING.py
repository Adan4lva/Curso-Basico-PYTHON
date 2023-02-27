"""

Created on Sun 26 Feb 2023

By Adan Alvarez

"""

import time

nombre = "Adan"

apellido = "Alvarez"

dia = "24"

mes = "Nov"

año = "2000"

frase = "\n" + nombre + " " + apellido + "\n" + dia + "/" + mes + "/" + año + "\n\n"

# Imprimimos cada caracter en la variable string con un pequeño retraso
for caracter in frase:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
