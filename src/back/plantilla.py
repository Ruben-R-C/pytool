from jinja2 import Template

class Plantilla:
	def __init__(self):
		pass

	# 
	def procesarPlantilla(self):
		print('cominenzo')
		t = Template("Hello {{ something }}!")
		print(t.render(something="World"))

if __name__== "__main__":
	plan = Plantilla()
	#PRUEBA 1 - vemos el encoding de este archivo
	plan.procesarPlantilla()




