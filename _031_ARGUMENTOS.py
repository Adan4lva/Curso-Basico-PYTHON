"""

Created on fri 10 March 2023

By Adan Alvarez

"""
def colores(*args):
	print('\nEl color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.\n')



def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('\nEl resultado de sumar estos cinco números es:', resultado,"\n\n")


colores('rojo', 'azul')

suma(5, 7, 45, 8657, 3, 4)