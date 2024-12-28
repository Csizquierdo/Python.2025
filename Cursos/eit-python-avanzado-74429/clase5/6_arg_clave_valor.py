# Argumentos clave - valor


def mostrar(empresa: str, *args, **kwargs):
    print("Empresa:", empresa)
    print(args)
    print(kwargs)


mostrar("EDUIT", "otro dato", "más datos", nombre="Juan", apellido="Perez", edad=20)
