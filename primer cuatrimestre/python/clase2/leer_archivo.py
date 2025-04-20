'''

archivo = open('prueba.txt','r',encoding='utf8')
print(archivo.read())
'''
from clase2.manejoDeArchivos import archivo

# video 5, uso de la "a"

'''
archivo = open('prueba.txt','a',encoding='utf8')
print(archivo.read())
'''

# video 6, nos muestra las 15 primeras letras de la primer palabra

'''
archivo = open('prueba.txt','r',encoding='utf8')
#print(archivo.read())
print(archivo.read(16))
print(archivo.read(9))
'''

#nos muestra en pantalla
'''
Programamos con 
diferente
'''

#Tambien podemos leer las lineas conpletas con el metodo readline

'''
archivo = open('prueba.txt','r',encoding='utf8')
print(archivo.readline()) # las veces que lo repitamos saltará a la siguiente linea
print(archivo.readline())
'''

'''
esto nos muestra en consola:
Programamos con diferentes tipos de archivos, ahora en .txt. 

Los acentos son importantes para las palabras 

'''
# video 7
# video 8
# vamos a iterar cada una de las lineas del archivo , modificando el codigo del archivo leer_archivo.py
'''
archivo = open('prueba.txt','r',encoding='utf8')
for linea in archivo :
    print(linea) # ahora agregamos informacion al archivo que esa en "manejo_archivos"
'''

'''
ahora veremos otro caso, de otro metodo que regresa una lista 
'''
'''
archivo = open('prueba.txt','r',encoding='utf8')
for linea in archivo :
    print(archivo.readlines()[11]) # accedemos al archivo como si fuera una lista,le ponemos diferentes elementos, lo colcam
    # en el formato lista con los corchetes
'''

# video 9
#abrimos el archivo origina (creado en manejo_archivos.py en modo lectura
'''
archivo = open ('prueba.txt','r',encoding='utf8')
# Abrimos el archivo de destino en modo 'append' (agregar al final)
archivo2 = open('copia.txt','w', encoding='utf8')
# leemos el contenido del archivo original y lo describimos en el nuevo
archivo2.write(archivo.read())
#cerramos el primer archivo
archivo.close()
#cerramos el segundo archivo
archivo2.close()

print('se ha terminado el proceso de leer y copiar archivos.')
'''

#-------------------------------------------------------------
'''
1.5 Uso de with, archivos y contexto Manager Parte 1

primero vamos a iterar el archivo, cada una de las lineas
vamos a usar un ciclo for en archivo
vemos que se itera y se muestra cada uan de las lineas
 ahora vamos a ingresar informacion directa al archivo
 ¿que pasa si agregamos otra linea al archivo?
 
 
archivo = open ('prueba.txt','r',encoding='utf8')
for linea in archivo:
    print(linea)
    
observamos que con el ciclo corto se van a agregando lineas, ya vimos con read, con read line, y ahora con for

ahora vamos a ver otro metodo llamado readlines, que muestra todo en lista, separado por coma
accedemos al archivo como si fuera una lista


archivo = open ('prueba.txt','r',encoding='utf8')
for linea in archivo:
    print(archivo.readlines())
    
# recordemos que las listas separa en diferentes elemetnos, por lo que podemos acceder a dichos elementos (elemento 1, elemento 2,e tc)


archivo = open ('prueba.txt','r',encoding='utf8')
for linea in archivo:
    print(archivo.readlines()[11])
    
video 9- vamos a crear un nuevo archivo y vamos a vaciar el contenido del archivo existente,en este nuevo archivo
para esto vamos a anexar informacion (no se va a sobreescribir

copia.txt abierto en modo append
si el archivo no existe lo crea, si existe anexa la informacion
tambien aprenderemos a crear una copia del archivo original

'''


