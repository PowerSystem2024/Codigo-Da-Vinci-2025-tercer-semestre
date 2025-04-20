'''
1.5 Uso de with, archivos y contexto Manager Parte 1
creamos el archivo archivos_con_with
hemos creado un archivo para usar el with y el manejod e archivs
siempre debemos
- abrir un archivo con el metodo open
- y cerramos con el metodo close
si no lo cerramos, python lo hace de manera automatica, pero hay qe hacerlo como buena practica
es importante al momento de hacer pruebas.

al trabajar con archivos debe tener el TRY Catch tambien, tambien con el finally

-pero ahora existe una sintaxis simplificada para cerrar los archivos y se lo conoce como "manejo de contexto with"
que lo abre y lo cierra, ya no es necesario el try catch ni el finally
se lo hace asi, se usa
- el metodo ENTER (donde se abre el archivo)
- y el metodo que cierra se llama exit

# manejo de contexto with: sintaxis simplificada
with open('prueba.txt','r',encoding='utf8') as archivo: #abrimos el archivo con el uso de caract
    print(archivo.read())


1.6 Uso de with, archivos y contexto Manager Parte 2
'''

from clase2.manejo_archivos import manejo_archivos

with manejo_archivos('prueba.txt') as archivo:
    print(archivo.read()) #una vez que lee el archivo , sale del metodo enter, y lee manejo_archivos

