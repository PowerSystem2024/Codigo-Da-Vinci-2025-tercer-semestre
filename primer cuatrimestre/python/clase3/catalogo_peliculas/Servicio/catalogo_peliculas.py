import os

class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula):
        with open(CatalogoPeliculas.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    @staticmethod
    def listar_peliculas():
        if os.path.exists(CatalogoPeliculas.ruta_archivo):
            with open(CatalogoPeliculas.ruta_archivo, "r", encoding="utf-8") as archivo:
                peliculas = archivo.readlines()
                for i, pelicula in enumerate(peliculas, 1):
                    print(f"{i}. {pelicula.strip()}")
        else:
            print("No hay películas registradas.")

    @staticmethod
    def eliminar():
        if os.path.exists(CatalogoPeliculas.ruta_archivo):
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivo eliminado.")
        else:
            print("El archivo no existe.")
