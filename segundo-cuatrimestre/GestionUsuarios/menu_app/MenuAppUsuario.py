from usuario_dao.UsuarioDao import UsuarioDao
from usuario.Usuario import Usuario
from getpass import getpass


class MenuAppUsuario:
    @staticmethod
    def mostrar_menu():
        print("\n" + "=" * 50)
        print(" MENÚ PRINCIPAL ".center(50))
        print("=" * 50)
        print("1. Listar usuarios")
        print("2. Agregar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

    @classmethod
    def ejecutar(cls):
        while True:
            cls.mostrar_menu()
            opcion = input("Seleccione una opción (1-5): ")

            if opcion == '1':
                cls.listar_usuarios()
            elif opcion == '2':
                cls.agregar_usuario()
            elif opcion == '3':
                cls.actualizar_usuario()
            elif opcion == '4':
                cls.eliminar_usuario()
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    @classmethod
    def listar_usuarios(cls):
        print("\nListado de usuarios:")
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            print(usuario)

    @classmethod
    def agregar_usuario(cls):
        print("\nAgregar nuevo usuario:")
        username = input("Username: ")
        password = getpass("Password: ")
        usuario = Usuario(username=username, password=password)
        registros_insertados = UsuarioDao.insertar(usuario)
        print(f"Registros insertados: {registros_insertados}")

    @classmethod
    def actualizar_usuario(cls):
        print("\nActualizar usuario:")
        id_usuario = int(input("ID del usuario a actualizar: "))
        username = input("Nuevo username: ")
        password = getpass("Nuevo password: ")
        usuario = Usuario(id_usuario=id_usuario, username=username, password=password)
        registros_actualizados = UsuarioDao.actualizar(usuario)
        print(f"Registros actualizados: {registros_actualizados}")

    @classmethod
    def eliminar_usuario(cls):
        print("\nEliminar usuario:")
        id_usuario = int(input("ID del usuario a eliminar: "))
        usuario = Usuario(id_usuario=id_usuario)
        registros_eliminados = UsuarioDao.eliminar(usuario)
        print(f"Registros eliminados: {registros_eliminados}")
