"""
Script para automatizar tareas
Python_3
"""
from front.buscar import Buscar

class Menu:
	def __init__(self):
		print(" ")
		print("============= Util Tool =============")
		print("1: Buscar ")
		print("2: Plantilla (en construcion) ")
		print("3: Salir")
		x = input('--> ')
		if x == "1":
			Buscar()
			Menu()
		elif x == "2":
			pass
		else:
			return

menu = Menu()
