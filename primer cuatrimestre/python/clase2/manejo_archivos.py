'''
aqui pondremos en practica 1.6 Uso de with, archivos y contexto Manager Parte 2


'''

class manejo_archivos:
    def __init__(self,nombre):
        self.nombre = nombre

    def __enter__(self):
        print('obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre,'r',encoding ='utf8')#aqui estamos encapsulando todo el codigo dentro de main
        return self.nombre

    def __exit__(self, tipo_exception, valor_exception, traza_error):
        print('cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close() # cerramos el archivo