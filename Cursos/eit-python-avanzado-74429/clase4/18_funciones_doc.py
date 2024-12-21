def saludar(usuario: str) -> str:
    """Genera un mensaje de saludo para el usuario dado.

    Args:
        usuario (str): El nombre del usuario a saludar.

    Returns:
        str: Un mensaje de saludo personalizado.
    """
    mensaje = f"Hola, {usuario}!"
    return mensaje


nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar(nombre_usuario)
print(saludo)

# Imprimir la documentación de la función saludar
print(saludar.__doc__)
help(saludar)
