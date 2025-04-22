"""
En Python tenemos varios tipos de manejo de archivos, por ejemplo: podemos manejar archivos de tipo texto,
con extensiones txt, también podemos manejar archivos binarios, cómo pueden ser fotos, audio, video, etc. Así
que prácticamente cualquier tipo de archivo lo podemos trabajar con Python.
En esta clase vamos a ver cómo trabajar con archivos de tipo texto:


--------------------------------------------------------
video 1.1.A Introducción a lo que es el manejo de archivos
En python tenemos varias formas de manejar archivos tipo texto con extension .txt , o archivos binarios como fotos o imagenes

ahora veremos de tipo texto




"""
# declaramos una variable
# archivo = open('prueba.txt','w')
# la w es de write que significa escribir hacia el archivo
# para esta variable vamos a necestitar un metodo, usamos el metodo open, que debe estar dentro de un bloque Try catch
# dentro de la nueva carpeta se crea un archivo .txt , y si el archivo no existe ,se crea , y luego se cierra
'''
try:
    archivo = open('prueba.txt','w')
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() # con esto se debe cerrar el archivo

'''
'''
hasta ahora vimos como se ha creado el archivo en la solapa izquierda. recuerden que el archivo se crea en la misma carpeta.
Ahora lo que queremos hacer es agregar informacion al archivo.
debajo de open  usamos el metodo write,que es para lograr escribir en el archivo
escribimos una linea por cada write
'''

'''
try:
    archivo = open('prueba.txt','w')
    archivo.write('Programamos con diferentes tipos de archivos, ahora en .txt. \n')
    archivo.write('Con esto terminamos .')
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() # con esto se debe cerrar el archivo
'''


'''
1.2 Especificar el juego de caracteres de un archivo de texto
ahora vamos a especificar un juego de caracteres de un archivo de texto, por ejemplo, colocando una palabra con acento
'''
'''
try:
    archivo = open('prueba.txt','w',encoding='utf8')
    archivo.write('Programamos con diferentes tipos de archivos, ahora en .txt. \n')
    archivo.write('Los acentos son importantes para las palabras \n')
    archivo.write('como por ejemplo : acción , ejecución y produccion. \n')
    archivo.write('Con esto terminamos \n')

except Exception as e: # cargamos el tipo de excepcion
    print(e)
finally: #siempre se ejecuta
'''

    #archivo.close() # con esto se debe cerrar el archivo
# archivo.write('todo quedo perfecto') -- este es un error

# ahora, si salgo del TRy y escribo en la linea 67
# archivo.write('todo quedo perfecto')
#esto me da error, porque elarchivo ya se ha cerrado al ejecutarse en la linea 66 el finally, despues del finally no
# podemos seguir trabajando con el archivo

'''
1.3 Lectura de archivos
video 4-creamos el archivo "leer_archivo"

lo que hace en este video el profe es trabajar sin el Try-catch
para leer un archivo podemos hacerlo de varias maneras, por ejemplo con read,que es para leer informacion de un archivo
es por default,
abre un archivo para lectura y manda un error si ese archivo no existe.

con el metodo open buscamos el archivo
ponemos r de read (aqui pondremos los diferentes modos, antes pusimos la w , ahora ponemos la r)
ponemos el encoding, usamos un juego de caracteres que soporta los acentos
ponemos un print que muestre el archivo .read

video 5 -
continuamos con las diferentes formas de lectura de archivos
ya vimos la letra r, la w, y ahora veremos la letra "a" que sirve para anexar informacion a un archivo que ya contiene 
informacion.
Es decir , abre un archivo para anexar o agregar mas informacion ( y crea el archivo en caso que NO exista)

es decir , las letras a usar son las : 
- r (read)
- a (append)
- w (write)
- x (para crear un archivo, pero regresa un error si el archivo no existe, es decir , nos manda una excepcion), 


'''

'''
try:
    archivo = open('prueba.txt','w',encoding='utf8')
    archivo.write('Programamos con diferentes tipos de archivos, ahora en .txt. \n')
    archivo.write('Los acentos son importantes para las palabras \n')
    archivo.write('como por ejemplo : acción , ejecución y produccion. \n')
    archivo.write('las letras a usar son las : \n')
    archivo.write('- r (read,leer) \n')
    archivo.write('- a (append,anexa) \n')
    archivo.write('- w (write,escribe) \n')
    archivo.write('- x (para crear un archivo, pero regresa un error si el archivo no existe, es decir , nos manda una excepcion) \n')
    archivo.write('- t (esta es para texto o text \n')
    archivo.write('- b (esta es para archivos binarios\n')
    archivo.write('- w+  (esta es para leer y escribir ,son iguales que r+\n ')
    archivo.write('Saludos a todos los alumnos de la tecnicatura \n')
    archivo.write('Con esto terminamos \n')
except Exception as e: # cargamos el tipo de excepcion
    print(e)
finally: #siempre se ejecuta
    archivo.close()

'''
'''
1.4 Más formas de trabajar con archivos

vamos a iterar cada una de las lineas del archivo , modificando el codigo del archivo leer_archivo.py
'''
# video 9
'''
ahora vamos a abrir un nuevo archivo, y vamos a vaciar el archivo con el contenido existente, para esto vamos a anexar 
infomacion, de esta manera , se va a anexar mas informacion ala rchivo, si el mismo no existe lo crea y agrega la informa
cion, y sino lo
agrega la informacion directamente.
basicamente anexaremos ifnormacion ,y copiaremos a otro.

el nombre del archivo serà archivo2 en leer_archivo.py
'''
#primero escribimos el archivo original
'''
try:
    archivo = open('prueba.txt','w',encoding='utf8')
    archivo.write('Programamos con diferentes tipos de archivos, ahora en .txt. \n')
    archivo.write('Los acentos son importantes para las palabras \n')
    archivo.write('como por ejemplo : acción , ejecución y produccion. \n')
    archivo.write('las letras a usar son las : \n')
    archivo.write('- r (read,leer) \n')
    archivo.write('- a (append,anexa) \n')
    archivo.write('- w (write,escribe) \n')
    archivo.write('- x (para crear un archivo, pero regresa un error si el archivo no existe, es decir , nos manda una excepcion) \n')
    archivo.write('- t (esta es para texto o text \n')
    archivo.write('- b (esta es para archivos binarios\n')
    archivo.write('- w+  (esta es para leer y escribir ,son iguales que r+\n ')
    archivo.write('Saludos a todos los alumnos de la tecnicatura \n')
    archivo.write('Con esto terminamos \n')
except Exception as e: # cargamos el tipo de excepcion
    print(e)
finally: #siempre se ejecuta
    archivo.close()

'''


