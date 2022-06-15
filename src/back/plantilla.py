from jinja2 import Template # motor de plantillas
import re # expresiones regulares

class Plantilla:
	def __init__(self):
		pass

	#Añadimos la funcion mayus() a los strings
	def __addMayus(self, txt):
		class mayusString(str):
			def __init__ (self, value):
				self.value = value
			def mayus(self):
				return self.value[0].upper() + self.value[1:]

		if isinstance(txt, str):
			return mayusString(txt)
		elif isinstance(txt, dict): 
			for key, value in txt.items():
				txt[key] = self.__addMayus(value)
			return txt
		elif isinstance(txt, list):
			for i in range(len(txt)): 
				txt[i] = self.__addMayus(txt[i])
			return txt
		else:	
			return txt

	def __tryDeleteQuotationMarks(self, stringWithMarks):
		try:
			re.search("^'", stringWithMarks).group()
			return stringWithMarks[1:-1]
		except:
			pass
		try:
			re.search('^"', stringWithMarks).group()
			return stringWithMarks[1:-1]
		except:
			pass
		return stringWithMarks

	def __tryParseBoolean(self, stringOfBoolean):
		pass
		if (stringOfBoolean == "true" or stringOfBoolean == "True"):
			return True
		elif (stringOfBoolean == "false" or stringOfBoolean == "False"):
			return False
		else:
			return stringOfBoolean

	def __tryParseInt(self, stringOfInt):
		try:
			return int(stringOfInt)
		except:
			pass
		return stringOfInt


	def __removeNewLines(self, lineas):
		file = []
		for linea in lineas:
			linea = linea.strip()
			file.append(linea)
		return file


	def __createVariable(self, linea):
		if linea == "=VARIABLE=":
			pass
		elif (linea):
			#Leemos lineas y buscar variables
			variable = re.search(".*(?=\=)", linea).group()
			valor = re.search("(?<=\=).*", linea).group()
			#Creamos variables globales con cada una de la variables
			valor = self.__tryDeleteQuotationMarks(valor)
			#Aniadimos la funcion .mayus()
			valor = self.__addMayus(valor)
			globals()[variable] = valor
			
	def __createTable(self, linea):
				if linea == "=TABLA=":
					self.tabla = ""
					self.columnas = []
					self.tabla_datos = []
				elif (linea):
					#en la primera linea, leemos el nombre de la tabla
					if(not self.tabla):
						self.tabla = linea
					#en la segunda linea, leemos el nombre de las columnas
					elif(not self.columnas):
						self.columnas = linea.split(",")
					#leer los datos de la tabla
					else:
						contenido = linea.split(",")
						dic = {}
						for i, col in enumerate(self.columnas):
							contenido[i] = self.__tryDeleteQuotationMarks(contenido[i])	
							contenido[i] = self.__tryParseInt(contenido[i])
							contenido[i] = self.__tryParseBoolean(contenido[i])
							dic[col] = contenido[i]

						self.tabla_datos.append(dic)
				else:
					#Añadimos la funcion .mayus()
					self.tabla_datos = self.__addMayus(self.tabla_datos)
					#se graba en el espacio en blanco despues de la tabla de la plantilla
					globals()[self.tabla] = self.tabla_datos 

	def __createTemplate(self, linea):
		if linea == "=PLANTILLA=":
			self.plantilla = []
		elif (linea):
			self.plantilla.append(linea)
		else:
			#se graba en el espacio en blanco despues del template
			globals()['template'] = '\n'.join(self.plantilla)


	def readFile(self):
		fichero = open('gen/plantilla_MyBatis.txt', 'r')
		lineas = fichero.readlines()
		lineas = self.__removeNewLines(lineas)

		#dependiendo de la seccion procesamos la variable la tabla o la plantilla
		while lineas:
			if lineas[0] == "=VARIABLE=" or lineas[0] == "=TABLA=" or lineas[0] == "=PLANTILLA=":
				seccion = lineas[0]
			if seccion == "=VARIABLE=":
				self.__createVariable(lineas[0])
			elif  seccion == "=TABLA=":	
				self.__createTable(lineas[0])
			elif  seccion == "=PLANTILLA=":
				self.__createTemplate(lineas[0])
			lineas.pop(0)
		fichero.close()

		print("")
		print("id "+id)
		print("clase"+clase)
		print("\nelementos\n\n"+str(elementos))
		print("\ntemplate\n\n"+template)
		print("\nRESULT\n\n")
		t = Template(template)
		print(t.render(id=id,clase=clase,elementos=elementos))



if __name__== "__main__":
	plan = Plantilla()
	#PRUEBA 1 - vemos el encoding de este archivo
	#o = plan.procesarPlantilla()
	#print(o)

	#a = plan.__addMayus("ruta")
	#print(a.mayus())

	#b = plan.__addMayus({'hola':'casa','adios':'arbol'})
	#print(b['hola'].mayus())

	#c = plan.__addMayus([{'hola':'casa','adios':'arbol'},{'hola':'coche','adios':'furgo'}])
	#print(c[1]['adios'].mayus())

	d = plan.readFile()
