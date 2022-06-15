# Pytool
Script de escritorio para automatizar tareas reptitivas.

Posible funcionalidades:
- buscar archivo (que comiencen por, terminen contengan por tamaño encoding y que tengan la extension)
- buscar libreria de java (dependencias en uso)
- ver contenido de archivos compimidos jar ear zip rar ... 
- extraer los contenidos de las clases
- correo automatizar outlook (enviar correo, borrador)
- automatizar la creacion de excel
- buscar codigo muerto en java
- plantillas

# Iniciar APP (de forma rápida)

En Windows 
1. instalar python 3
2. ejecutar init.bat 

# Iniciar APP (paso a paso)

1. Comprobar que tenemos python 3
```
#En windows
python --version
#En Mac y Linux
python3 --version 
```

2. Iniciar entorno virtual
```
#En windows
python -m venv venv
#En Mac y Linux
python3 -m venv venv
```

3. Activar entorno virtual
```
#En windows
venv\Scripts\activate
#En Mac y Linux
source venv/bin/activate
```
Ahora, la consola comienza por (venv)
indicando que estamos en el entorno virtual


5. Instalar librería para ver el codec de los archivos
```
#Sin proxy
pip3 install charset-normalizer
#Usando el proxy proxy:8080
pip3 install --proxy=http://proxy:8080 charset-normalizer
```
[documentacion charset-normalizer](https://charset-normalizer.readthedocs.io/en/latest/user/getstarted.html)


6. Instalar librería para generar código apartir de plantillas
```
pip3 install Jinja2
```
[documentacion jinja2](https://jinja.palletsprojects.com/en/3.1.x/templates/#expressions)


6. Ejecutar main.py
```
#En Mac y Linux
venv/bin/python src/main.py
#En windows
python src/main.py
```
# Configurar entorno de desarrollo 

1. Instalar VS Code

2. Activar el interperte de VS Code
Para que el interprete sea el del entorno virtual
y no el python del sistema
VSCode -> View -> Command palette -> Python Select Interpreter 
Ahora al imiciar un archivo con la extersion .py 
en la esquina inferior derecha pondra el interprete de venv

# Documentacion plantillas Ninja2

https://jinja.palletsprojects.com/en/3.0.x/templates/
https://realpython.com/primer-on-jinja-templating/


# Ejemplo 1 de funcionalidad generador de plantillas para MyBatis 

```
       ********VARIABLES**********

bean = "Equipo"
paquete = "com.etc.model."

       ********MATRIZ**********

tablaMapeo
columnasSQL parametrosBean         key 
RESPOM   usuarioResponsablekey    true
CEQUIM   codigoEquipokey          true
EQUIPM   nombreEquipo             false
DEQUIM   descripcionEquipo        false
FALTAM   fechaAlta                false
USUARM   usuario                  false

       ********LISTA_DE_ETIQUETAS**********

            <<VARIABLES>>
            <<LOOP=nombreTabla>> de tablas
            <<LOOP=nombreTabla.IF.columan>> de tablas
            <<LOOP=nombreTabla.IF.NOT.columan>> de tablas
                <<NOT.PRINT.LAST>>
                <<NOT.PRINT.BEGIN>>
                <<ONLY.PRINT.LAST>>
                <<ONLY.PRINT.BEGIN>>
                <<INDEX>>
                <<INDEX+numero>>
            
       ********PLANTILLA**********

	<update id="update<<bean>>" parameterClass="<<paquete>><<bean>>">
		UPDATE CPDATD.GPFM
		SET       
    <<loop=tablaMapeo.if.key>>
        <<ifnot=key>>
            <<columnasSQL>> = #<<parametrosBean>>#,
        <<//ifnot>>
    <<//loop>>   
    WHERE
    <<loop=tablaMapeo.ifnot.key>>
    <<columnasSQL>> = #<<parametrosBean>>#<<notPrintLast>>, AND<<//notPrintLast>>
    <<//loop>>
	</update>
    
        ********CODIGO_GENERADO**********
    
    <update id="updateEquipo" parameterClass="com.etc.model.Equipo">
		UPDATE CPDATD.GPFM041
		SET
		EQUIPM = #nombreEquipo#,
		DEQUIM = #descripcionEquipo#,
		FALTAM = #fechaAlta#,
		USUARM = #usuario#,
		RESPOM = #usuarioResponsablekeyMostrar#
		WHERE CEQUIM = #codigoEquipokey#
		AND RESPOM = #usuarioResponsablekey#
	</update>
    
```  

# Ejemplo 2 Generar Beans enlazados


``` 
package com.example;  
public class Employee {  
private String name;  
private String id;  
 
public String getName() {  
    return name;  
}  
public void setName(String name) {  
    this.name = name;  
}  
public String getId() {  
    return id;  
}  
public void setId(String id) {  
    this.id = id;  
}  
}  
``` 