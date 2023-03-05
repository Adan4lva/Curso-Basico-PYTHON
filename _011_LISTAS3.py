"""

Created on sat 5 March 2023

By Adan Alvarez

"""

import time

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("\nLista original:")

for elemento in colores:
    time.sleep(0.2)
    print(elemento)

del colores[1]
del colores[3]
del colores[4]
del colores[-3]

print("\nLista modificada:")
for elemento in colores:
    time.sleep(0.2)
    print(elemento)

print("\n\n")