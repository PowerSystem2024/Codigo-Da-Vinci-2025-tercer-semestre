"""
dependiendo del tipo de error, es el tipo de excepcion que usaremos
# Jerarquía de Excepciones en Python:
#
# 1. BaseException (Clase base /clase PADRE de y para todas las excepciones en Python)
#    └── 2. Exception (Clase base para todas las excepciones "normales")
#        ├── 3. ArithmeticError (Errores matemáticos)
#        │   └── 4. ZeroDivisionError (División por cero)
#        ├── 3. OSError (Errores relacionados con el sistema operativo)
#        │   ├── 4. FileNotFoundError (Archivo no encontrado)
#        │   └── 4. PermissionError (Error de permisos)
#        ├── 3. RuntimeError (Errores de ejecución)
#        ├── 3. LookupError (Errores relacionados con búsqueda)
#        │   ├── 4. IndexError (Índice fuera de rango)
#        │   └── 4. KeyError (Clave no encontrada en un diccionario)
#        ├── 3. SyntaxError (Errores de sintaxis)
#        │   └── 4. IndentationError (Error en la indentación)
#
# Esta jerarquía es útil para entender cómo se manejan las excepciones en Python
# y cómo podemos crear bloques de manejo de errores utilizando excepciones específicas
con EXCEPTION capturamos cualquier de las excepciones de abajo.


ahora lo que haremos es envolver nuestro codigo en un bloque TRY
"""


#video 2:.2 Procesamiento de excepciones
#ahora vamos a agregarle variables al bloque de codigo anterior

"""try:
    10/0
except Exception as e:
    print(f'ocurrio un error : {e} ')
------------------------------------------
resultado = None
a = 10
b = 0
try:
    resultado = a / b #modificamos
except Exception as e:
    print(f'ocurrio un error : {e} ')
print(f'el resultado es :{resultado}')
print('seguimos ...') """

# ahora que pasa si a la variable "a" le asignamos un valor en cadena en lugar de un valor numerico, ahi usamos
# ZeroDivisionError y en a = '10' que es una cadena

'''resultado = None
a = '10'
b = 0
try:
    resultado = a / b #modificamos
except ZeroDivisionError as e:
    print(f'ocurrio un error : {e} ')
print(f'el resultado es :{resultado}')
print('seguimos ...')'''

# nos saldra el error que pusimos un string en lugar de un int,no tiene soporte para tipos string y tipos enteros.
# o sea , o son todos numericos o son todos string, lo importante es no mezclar, o sino usar las clases padres de excepciones
# Por eso es conveniente usar las clases de Excepciones padres
# que cubren mas errores que las especificas como ZERODIVISIONERROR

#----------------------------------------------
#1.3 Procesar clases de exception más específicas
#ahora usamos Zerodivisionerror.Vamos a ir viendo lo que son las jerarquias con este ejemplo

'''resultado = None
a = 5
b = 7
try:
    resultado = a / b #modificamos
except TypeError as e:
    print(f'TypeError - ocurrio un error : {type(e)} ')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error : {type(e)} ')
except Exception as e:
    print(f'Exception - ocurrio un error : {type(e)} ')
print(f'el resultado es :{resultado}')
print('seguimos ...')'''

# probamos con a = '10'
#luego probamos con a = 7 y b = 5
# de esta manera el error no detiene al programa
# ----------------------------------------------------------------------------------
# 1.4 Más de procedimientos de excepciones
# podemos poner las variables adentro del TRY, y ademas podemos pedirlas al usuario, de esta manera, con  input

'''resultado = None
try:
    a = int(input('digite el primer numero :'))
    b = int(input('digite el segundo numero :'))
    resultado = a / b #modificamos
except TypeError as e:
    print(f'TypeError - ocurrio un error : {type(e)} ')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error : {type(e)} ')
except Exception as e:
    print(f'Exception - ocurrio un error : {type(e)} ')
print(f'el resultado es :{resultado}')
print('seguimos ...')'''

# si ingresamos a = 3 y b = 3 , nos arroja resultado
# si ingresamos a = a  nos arroja el resultado:Exception - ocurrio un error : <class 'ValueError'>
# el resultado es :None

# si ingresamos a = 3 y b = 0 , nos arroja resultado ZeroDivisionError - ocurrio un error : <class 'ZeroDivisionError'>
# esto significa que siempre necesitamos variables globales, dentro del TRY ¿?

#
#1.5 Bloques else y finally al manejar excepciones
# el bloque ELSE unicamente se va a ejecutar en caso de que no hayan lanzado la excepcion
#

'''resultado = None
try:
    a = int(input('digite el primer numero :'))
    b = int(input('digite el segundo numero :'))
    resultado = a / b #modificamos
except TypeError as e:
    print(f'TypeError - ocurrio un error : {type(e)} ')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error : {type(e)} ')
except Exception as e:
    print(f'Exception - ocurrio un error : {type(e)} ')
else:
    print ("no se arrojo ninguna excepcion")
finally:# siempre se va a ejecutar
    print("ejecucion de este bloque finally")
print(f'el resultado es :{resultado}')
print('seguimos ...')'''
# si pongo a= 8 y b= 0 , da ZeroDivisionError - ocurrio un error : <class 'ZeroDivisionError'>
#---------------------------------------------------------------------------------------
#1.6 Creación de clases de Exception personalizadas

from NumerosIgualesException import NumerosIgualesException
resultado = None
try:
    a = int(input('digite el primer numero :'))
    b = int(input('digite el segundo numero :'))
    if a == b:
        raise NumerosIgualesException('son numeros iguales') # raise nos permite disparar o llamar la excepcion
    resultado = a / b #modificamos
except TypeError as e:
    print(f'TypeError - ocurrio un error : {type(e)} ')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error : {type(e)} ')
except Exception as e:
    print(f'Exception - ocurrio un error : {type(e)} ')
else:
    print ("no se arrojo ninguna excepcion")
finally:# siempre se va a ejecutar
    print("ejecucion de este bloque finally")
print(f'el resultado es :{resultado}')
print('seguimos ...')
#probamos con a = 7 y b = 7.Se ejecuta hasta la nueva linea, creando una clase de excepcion