"""

Created on fri 3 March 2023

By Adan Alvarez

"""

import time

frase = "\n\n-Python.\n-JavaScript.\n-Java.\n-PHP.\n-TypeScript.\n-SQL.\n-COBOL.\n-C++.\n-Ensamblador.\n\n"

# Imprimimos cada caracter en la variable string con un pequeño retraso
for caracter in frase:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
