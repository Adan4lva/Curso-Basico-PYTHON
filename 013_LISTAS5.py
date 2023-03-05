"""

Created on sun 5 March 2023

By Adan Alvarez

"""

import time

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("\nLista original:")

for elemento in colores:
    time.sleep(0.2)
    print(elemento)

color1 = colores.pop(1)
color2 = colores.pop(7)

colores_guardados = [color1, color2]


print("\nLista modificada:")
for elemento in colores:
    time.sleep(0.2)
    print(elemento)

print("\nElementos eliminados: ")
print(colores_guardados)

print("\n\n")
