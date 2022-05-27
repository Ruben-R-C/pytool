from os import path,walk,listdir 
import re # replace regex
from charset_normalizer import from_path

class Buscar:
	def __init__(self):
		#self.ruta=None
		pass

	# Buscar en path
	def listar_elementos_carpeta_recursiva(self, ruta):
		self.__comprobar(ruta)
		directorios = []
		archivos = []
		for raiz, directorio, archivo in walk(self.ruta):
			for file in archivo:
				archivos.append(path.join(raiz, file))
			for dir in directorio:
				directorios.append(path.join(raiz, dir))
		elementos = {'directorios': directorios, 'numero_directorios': {len(directorios)}, 
		        'archivos': archivos,'numero_archivos': {len(archivos)}}
		return elementos


	def listar_elementos_carpeta_principal(self, ruta):
		self.__comprobar(ruta)
		elementos_principales=listdir(ruta)
		elementos = {'elementos': elementos_principales, 'numero_elementos': len(elementos_principales)}
		return elementos

	# Ver elementos de un directorio
	def ver_codec_archivo(self, ruta):
		self.__comprobar(ruta)
		f=from_path(ruta).best()
		return f.encoding


	#Quitamos contrabarras y comprobamos que existe
	def __comprobar(self, ruta):
		ruta = re.sub(r'\\', '/', ruta)
		if not path.exists(ruta):
			print(f"ERROR: La ruta {ruta} no existe.")
			quit()
		else:
			self.ruta = ruta



#devuelve todo el contenido <- listar(tipo(ambos, directorio, archivo) ruta)
#ver_carpeta(ruta)
#Buscar (tipo(ambos, directorio, archivo), nombre-opcional, extension-opcional)
#Bucar_por_contenido(contenido,  nombre-opcional, extension-opcional)
#Buscar_codec(ruta)
#Buscar_librerias(ruta, libreria, )


if __name__== "__main__":
	buscar = Buscar()
	#PRUEBA 1 - vemos el encoding de este archivo
	print("PRUEBA 1 ", buscar.ver_codec_archivo('/Users/ruben/desktop/pytool/README.md'))
	#PRUEBA 2 - vemos los elemtos de un directorio
	print("PRUEBA 2 ", buscar.listar_elementos_carpeta_principal('/Users/ruben/desktop/pytool'))
	#PRUEBA 3 - ver todos los archivos y carpetas de manera recursiva
	print("PRUEBA 3 ", buscar.listar_elementos_carpeta_recursiva('./test'))

