
from back.buscar import Buscar
from back.tipo_elemento import Tipo_elemento

#from enum import Enum 

class Eliminar:
	
	def __init__(self):
		#Tipo_elemento = Enum('Tipo', 'archivos_ficheros solo_archivos solo_ficheros')
		self.ruta = None
		self.tipo = None
		print("============= ELIMINAR =============")
		print("1. Eliminar archivos y ficheros")
		print("2. Eliminar solo archivos")
		print("3. Eliminar solo ficheros")
		print("4. Procesos")
		print("5. Salir")
		x = input('--> ')
		if x == "1":
			self.tipo = Tipo_elemento['archivos_ficheros']
			self.delete_in_path()
		if x == "2":
			self.delete_in_path()
		if x == "3":
			self.delete_in_path()
		if x == "4":		
			self.eliminar_proceso()


	def delete_in_path(self):
		print("=============")
		self.ruta = input("La ruta del archivo es: ")
		print(self.ruta)
		self.delete_select_files()

	def delete_select_files(self):
		print("=============")
		#print("xx archivos, xx carpetas, xx con extension")
		print(f'La ruta xx tiene {self.ruta}')
		#Buscar.buscar_in_path(self.ruta)
		print("Si son menos de 10 se muestran aquí")		
		print("1. Añadir filtro")
		print("2. Ver todos")
		print("3. Eliminar")
		print("4. Volver")
		x = input('--> ')
		if x == "1":
			self.delete_add_filter()
		#if x == "2":
			#ver todos
		if x == "3":
			self.delete_files()
		#if x == "4":
			#Menu()

	def delete_files(self):
		print("=============")
		print(f"¿Seguro que quieres eliminar en {self.ruta} los siguientes xx archivos?")

	def delete_add_filter():
		print("=============")
		print("El nombre del archivo es ")
		print("La ruta")
		print("La ruta")
		print("La ruta")
		x = input('--> ')
		if x == "1":
			print("m")
		if x == "2":
			print("m")
		if x == "3":
			print("m")

	def eliminar_buscar_proceso(self):
		print("=============")
		print("1. Buscar procesos por nombre")
		print("2. Buscar por ID")
		x = input('--> ')
		self.eliminar()
		#if existen procesos:
		#	eliminar()
		#else:
		#	print("No existe ningun proceso")
		#elige volver a inicio o buscar otro proceso
	
	def eliminar_proceso():
		print("=============")
		print("¿Seguro que quieres eliminar los siguientes procesos?")
		print("1. xxxxxxxxx")
		print("2. xxxxxxxxx")
		print("2. xxxxxxxxx")
		x = input('--> ')
		if x == "1":
			print("Eliminamos el proceso XXXXXXXX")

	def eliminar_excluir_incluir():
		print("=============")
		print("1. Excluir")
		print("2. Incluir")
		x = input('--> ')
		if x == "1":
			print("m")
		if x == "2":
			print("m")
