#importar desde ruta principal
import sys
from pathlib import Path
d = Path(__file__).parents[1]
sys.path.append(str(d))

import back.buscar as buscar
from back.tipo_elemento import Tipo_elemento

class Buscar:
	def __init__(self):
		self.ruta = None
		self.tipo = None
		print(" ")
		print("============= BUSCAR =============")
		print(d)
		print("1. archivos y ficheros")
		print("2. solo archivos")
		print("3. solo ficheros")
		print("4. procesos")
		print("Enter - volver")
		x = input('--> ')
		if x == "1":
			self.tipo = Tipo_elemento['archivos_ficheros']
			self.search_in_path()
		if x == "2":
			self.search_in_path()
		if x == "3":
			self.search_in_path()
		if x == "4":		
			pass


	def search_in_path(self):
		print(" ")
		self.ruta = input("La ruta del archivo es: ")
		#BORRAR ->
		self.ruta='test'
		print('')
		b = buscar.Buscar()
		elem_recur = b.listar_elementos_carpeta_recursiva(self.ruta)
		elem_prin = b.listar_elementos_carpeta_principal(self.ruta)

		print("")
		print("<<<<<<  RESUMEN >>>>>>")
		print('- Directorio ----------- ',self.ruta)
		if elem_prin['numero_elementos'] < 10:
			print('- Contenido ------------: ',elem_prin['elementos'])
		print("- Los archivos son ----- ", elem_recur['numero_archivos'])
		print("- Los directorios son -- ", elem_recur['numero_directorios'])
		print("- El Total es ---------- ")
		print(' ')		
		print("1. Añadir filtro")
		print("2. Ver todos")
		print("3. Eliminar")
		print("4. Volver")
		x = input('--> ')


	def search_add_filter():
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

	def search_process(self):
		print("=============")
		print("1. Buscar procesos por nombre")
		print("2. Buscar por ID")
		x = input('--> ')
		self.eliminar()


#Cambiar extension
#Cambiar encoding