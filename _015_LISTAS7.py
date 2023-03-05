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

colores.insert(-4, 'magenta')
colores.insert(-1, 'turquesa')


print("\nLista modificada:")
for elemento in colores:
    time.sleep(0.2)
    print(elemento)

print("\n\n")
