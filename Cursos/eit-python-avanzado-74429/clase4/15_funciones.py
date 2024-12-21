def saludar():
    print("Hola, ¿cómo estás?")


def despedir():
    print("Hasta luego, que te vaya bien")


# saludar()
# despedir()

lista_funciones = [saludar, despedir]
for funcion in lista_funciones:
    funcion()
