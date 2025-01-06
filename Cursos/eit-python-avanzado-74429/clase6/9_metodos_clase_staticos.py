from typing import Self


class Usuario:
    usuarios: list[Self] = []

    def __init__(self, nombre: str, contraseña: str):
        self.nombre = nombre
        self.contraseña = contraseña
        Usuario.usuarios.append(self)

    @classmethod
    def mostrar_usuarios(cls):
        for usuario in cls.usuarios:
            print(f"Nombre: {usuario.nombre}, Contraseña: {usuario.contraseña}")

    @staticmethod
    def info():
        print("Bienvenido!")


usuario_1 = Usuario("Juan", "1234")
usuario_2 = Usuario("Pedro", "5678")

Usuario.mostrar_usuarios()
Usuario.info()
