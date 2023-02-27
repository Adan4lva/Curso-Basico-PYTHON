"""

Created on Sun 26 Feb 2023

By Adan Alvarez

"""

import time

# Definimos la variable string
variable = "\nEste es mi primer programa en PYTHON\n\n"
num1 = 2000
num2 = 23
num = num1 + num2
var2 = "\nCoded on earth by humans...\n"

# Imprimimos cada caracter en la variable string con un pequeño retraso
for caracter in variable:
    print(caracter, end='', flush=True)
    time.sleep(0.05)

print(num)

for caracter in var2:
    print(caracter, end='', flush=True)
    time.sleep(0.05)