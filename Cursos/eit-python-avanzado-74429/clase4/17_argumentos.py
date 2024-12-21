def saludar(saludo: str, nombre: str) -> None:
    print(f"{saludo} {nombre}")


saludar("Hola!", "Juan")  # argumentos por posición
saludar(nombre="Pedro", saludo="Buenos días!")  # argumentos por nombre
