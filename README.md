# Pytool
Script de escritorio para automatizar tareas reptitivas.

Posible funcionalidades:
- buscar archivo que comiencen por, que terminen por, que contengan algo y por extension, dentro de zip, ver resumen y arbol 
- jar zip , buscar libreria de java, ver arbol de jar zip
- pojo , extraer datos, pasar a excel, mapear excel a bean con plantilla
- correo automatizar outlook enviar correo, borrador
- excel automatizar algo
- buscar codigo muerto en forma de arbol 
- buscar por tamaño y por encoding
- plantillas

# Iniciar APP

1. Comprobar que tenemos python 3
python3 --version 

2. Iniciar entorno virtual
```
python3 -m venv venv
```
Esto

3. Si usamos VS Code activar el interperte 
VSCode -> View -> Command palette -> Python Select Interpreter 
Ahora al imiciar un archivo con la extersion .py 
en la esquina inferior derecha pondra el interprete de venv

4. Activar entorno virtual
```
#En windows
\venv\Scripts\activate.bat
#En Mac y Linux
source venv/bin/activate
```

5. Instalar librería para ver el codec de los archivos
Usa la etiqueta proxy, solo en caso necesario
```
pip3 install --proxy=http://proxy:8080 charset-normalizer
```
documentacion -> https://charset-normalizer.readthedocs.io/en/latest/user/getstarted.html

6. Ejecutar main.py
```
venv/bin/python src/main.py
```

# Ejemplo de funcionalidad generador de plantillas para MyBatis y Beans

       ********VARIABLES**********

bean = "Equipo"
paquete = "com.etc.model."

       ********MATRIZ**********

tablaMapeo
columnasSQL parametrosBean            key 
RESPOM   usuarioResponsablekey    true
CEQUIM   codigoEquipokey          true
EQUIPM   nombreEquipo             false
DEQUIM   descripcionEquipo        false
FALTAM   fechaAlta                false
USUARM   usuario                  false

       ********LISTA_DE_ETIQUETAS**********

            <<VARIABLES>>
            <<LOOP>> de tablas
                <<IF>>
                <<IFNOT>>
                <<NOTLAST>>
                <<INDEX>>
            
       ********PLANTILLA**********


	<update id="update<<bean>>" parameterClass="<<paquete>><<bean>>">
		UPDATE CPDATD.GPFM
		SET       
    <<loop=tablaMapeo>>
        <<ifnot=key>>
            <<columnasSQL>> = #<<parametrosBean>>#,
        <<//ifnot>>
    <<//loop>>   
    WHERE
    <<if=key>>
    <<columnasSQL>> = #<<parametrosBean>>#<<notlast>>, AND<<//notlast>>
    <<//if>>
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
    
   
----------------------
