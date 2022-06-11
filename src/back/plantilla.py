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


	def readFile2(self):
		fichero = open('gen/plantilla_MyBatis.txt', 'r')
		lineas = fichero.readlines()

		#quitar saltos de linea
		file = []
		for linea in lineas:
			linea = linea.strip()
			file.append(linea)

		#recoremos el archivo
		lineas = file
		while lineas:
			#extraer seccion
			if lineas[0] == "=VARIABLE=" or lineas[0] == "=TABLA=" or lineas[0] == "=PLANTILLA=":
				seccion = lineas[0]
				#lineas.pop(0)

			#extraer variable
			if seccion == "=VARIABLE=":
				if lineas[0] == "=VARIABLE=":
					pass
				elif (lineas[0]):
					#Leemos lineas y buscar variables
					variable = re.search(".*(?=\=)", lineas[0]).group()
					valor = re.search("(?<=\=).*", lineas[0]).group()
					#Creamos variables globales con cada una de la variables
					globals()[variable] = valor
				lineas.pop(0)

			#extraer tabla
			if  seccion == "=TABLA=":	
				if lineas[0] == "=TABLA=":
					tabla = ""
					columnas = []
					tabla_datos = []
				elif (lineas[0]):
					#en la primera linea, leemos el nombre de la tabla
					if(not tabla):
						tabla = lineas[0]
					#en la segunda linea, leemos el nombre de las columnas
					elif(not columnas):
						columnas = lineas[0].split(",")
					#leer los datos de la tabla
					else:
						contenido = lineas[0].split(",")
						dic = {}
						for i, col in enumerate(columnas):
							#si es un string quitamos entrecomidado
							try:
								print(re.search("^'", contenido[i]).group())
								contenido[i] = contenido[i][1:-1]
							except:
								pass
							try:
								print(re.search('^"', contenido[i]).group())
								contenido[i] = contenido[i][1:-1]
							except:
								pass							
							# #si es un booleano
							if (contenido[i] == "true" or contenido[i] == "True"):
								contenido[i] = True
							if (contenido[i] == "false" or contenido[i] == "False"):
								contenido[i] = False
							#si es un numero
							try:
								contenido[i] = int(contenido[i])
							except:
								pass					
							dic[col] = contenido[i]
						tabla_datos.append(dic)
				else:
					#se acaba la tabla
					globals()[tabla] = tabla_datos #Creamos una variable con el nombre de la tabla
				lineas.pop(0)

			#extraer plantilla
			if  seccion == "=PLANTILLA=":
				if lineas[0] == "=PLANTILLA=":
					plantilla = []
				elif (lineas[0]):
					#print("plantilla "+lineas[0])
					plantilla.append(lineas[0])
				else:
					#definimos la variable
					globals()['template'] = '\n'.join(plantilla)
				lineas.pop(0)
		
		fichero.close()

		print("")
		print("id "+id)
		print("clase"+clase)
		print("\nelementos\n\n"+str(elementos))
		print("\ntemplate\n\n"+template)
		print("")
		t = Template(template)
		print(t.render(id=id,clase=clase,elementos=elementos))





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
