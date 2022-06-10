from statistics import linear_regression
from jinja2 import Template # motor de plantillas
import re # expresiones regulares

class Plantilla:
	def __init__(self):
		pass



	#Añadimos la funcion mayus() a los strings
	def addMayus(self, e):
		class mayusString(str):
			def __init__ (self, value):
				self.value = value
			def mayus(self):
				return self.value[0].upper() + self.value[1:]

		if isinstance(e, str):
			return mayusString(e)
		elif isinstance(e, dict): 
			for key, value in e.items():
				e[key] = self.addMayus(value)
			return e
		elif isinstance(e, list):
			for i in range(len(e)): 
				e[i] = self.addMayus(e[i])
			return e
		else:	
			return e


	def procesarPlantilla(self):
		elementos=[
			{'columnasSQL': "RESPOM", 'parametrosBean': "usuarioResponsablekey", 'key': True},
			{'columnasSQL': "CEQUIM", 'parametrosBean': "codigoEquipokey", 'key': True},
			{'columnasSQL': "EQUIPM", 'parametrosBean': "nombreEquipo", 'key': False},
			{'columnasSQL': "DEQUIM", 'parametrosBean': "descripcionEquipo", 'key': False},
			{'columnasSQL': "FALTAM", 'parametrosBean': "fechaAlta", 'key': False}]
			
		id="updateEquipo" 
		clase="com.etc.model.Equipo"

		elementos = self.addMayus(elementos)
		id = self.addMayus(id)
		clase = self.addMayus(clase)

		t = Template("""
	    <update id="{{id}}" parameterClass="{{clase}}">
		UPDATE CPDATD.GPFM041
		SET
		{% for elemento in elementos %}{% if not elemento.key %} {{elemento.columnasSQL}}  = #{{elemento.parametrosBean}}#, {% endif %} 
		{% endfor %}
		{% for elemento in elementos %}{% if elemento.key %} WHERE {{elemento.columnasSQL}}  = #{{elemento.parametrosBean}}#  {% endif %} 
		{% endfor %}
		</update>
		""")

		h = Template("""
		package com.example;  
		public class {{id}} { 
			{% for elemento in elementos %}
				private String {{elemento.parametrosBean}};  {% endfor %} 	
			{% for elemento in elementos %}
				public String get{{elemento.parametrosBean.mayus()}}() {  
    				return {{elemento.parametrosBean}};  
				}  

				public void set{{elemento.parametrosBean.mayus()}}(String {{elemento.parametrosBean}}) {  
		    		this.{{elemento.parametrosBean}} = {{elemento.parametrosBean}};  
				} 
			{% endfor %} 
		""")

		return h.render(elementos=elementos,id=id,clase=clase)



	def readFile(self):
		fichero = open('gen/plantilla_MyBatis.txt', 'r')
		lineas = fichero.readlines()
		tpo=''
		idx=0
		var=0
		tbl=0
		pln=0
		for linea in lineas:
		
			linea = linea.strip()
			
			if linea == "=VARIABLE=":
				print(linea)
				tpo='variable' 
				idx += 1
			elif  linea == "=TABLA=":
				print(linea)
				tpo='tabla' 
				idx += 1
				tbl = 0 
			elif  linea == "=PLANTILLA=":
				print(linea)
				tpo='plantilla' 
				idx += 1
			elif  tpo == "variable":
				if (linea):
					#Leemos lineas y buscar variables
					variable = re.search(".*(?=\=)", linea).group()
					valor = re.search("(?<=\=).*", linea).group()
					print("variable:  "+variable+"  valor:  "+valor)
					#Creamos variables globales con cada una de la variables
					globals()[variable] = valor
					
			elif  tpo == "tabla":
				if (linea):
					tbl += 1
					#en la primera linea, leemos el nombre de la tabla
					if(tbl == 1):
						tabla = linea
					#en la segunda linea, leemos el nombre de las columnas
					if(tbl == 2):
						columnas = linea.split(",")
						print(columnas)
					#leer los datos de la tabla
					if(tbl >= 3):
						contenido = linea.split(",")
						dic = {}
						for id, col in enumerate(columnas):
							dic[col] = contenido[id]
						print(dic)
						globals()[tabla] = [] #Creamos una variable con el nombre de la tabla que apunta a una lista vacia
			elif  tpo == "plantilla":
				#print(linea + " tpo -> "+tpo+"  "+str(idx))
				pass
		fichero.close()


	def readFile2(self):
		fichero = open('gen/plantilla_MyBatis.txt', 'r')
		lineas = fichero.readlines()

		#quitar saltos de linea
		file = []
		for i,linea in enumerate(lineas):
			linea = linea.strip()
			file.append(linea)
		print(file)

		#recoremos el archivo
		lineas = file
		for li in file:

			#extraer seccion
			if li == "=VARIABLE=" or li == "=TABLA=" or li == "=PLANTILLA=":
				print(linea)
				seccion = linea




		fichero.close()







if __name__== "__main__":
	plan = Plantilla()
	#PRUEBA 1 - vemos el encoding de este archivo
	o = plan.procesarPlantilla()
	#print(o)

	a = plan.addMayus("ruta")
	#print(a.mayus())

	b = plan.addMayus({'hola':'casa','adios':'arbol'})
	#print(b['hola'].mayus())

	c = plan.addMayus([{'hola':'casa','adios':'arbol'},{'hola':'coche','adios':'furgo'}])
	#print(c[1]['adios'].mayus())

	d = plan.readFile2()
