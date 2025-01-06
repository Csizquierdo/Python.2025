class Usuario:
    usuario = "admin"  # variable de clase

    def __init__(self, nombre: str, contraseña: str):
        self.nombre = nombre
        self.contraseña = contraseña


usuario_1 = Usuario("Juan", "1234")
usuario_2 = Usuario("Pedro", "5678")

print(usuario_1.nombre, usuario_1.contraseña, usuario_1.usuario)
print(usuario_2.nombre, usuario_2.contraseña, usuario_2.usuario)
