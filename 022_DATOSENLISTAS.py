"""

Created on sun 5 March 2023

By Adan Alvarez

"""

colores = input('\nIntroduce un color:\n')
tupla_colores = ('rojo', 'azul', 'verde', 'amarillo')

if colores in tupla_colores[0]:
	print('\nEl color rojo está admitido')
elif colores in tupla_colores[1]:
	print('\nEl color azul está admitido')
elif colores in tupla_colores[2]:
	print('\nEl color verde está admitido')
elif colores in tupla_colores[3]:
	print('\nEl color amarillo está admitido')
else:
	print('\nColor no admitido')

print('\n\n')
