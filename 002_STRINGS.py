"""

Created on Sun 26 Feb 2023

By Adan Alvarez

"""

import time

texto1 = "Se puede almacenar con comillas dobles"

texto2 = 'Tambien con comillas simples'

frase = '\n"print()" se utiliza para imprimir valores en la consola.\n\n'

# Imprimimos cada caracter en la variable string con un pequeño retraso
for caracter in frase:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
