"""

Created on fri 10 March 2023

By Adan Alvarez

"""

class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('\nNombre:', self.nombre, '\nApellidos:', self.apellidos, "\n\n")

usuario001 = Usuario()

usuario001.nombre = 'Adan'
usuario001.apellidos = 'Alvarez Barajas'

usuario001.imprime_datos()
