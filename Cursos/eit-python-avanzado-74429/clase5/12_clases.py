"""
variables y funciones: snake_case
clases: UpperCamelCase
"""


class Ciudad:
    def __init__(self, nombre: str, poblacion: int):  # método constructor
        print("Se creó un objeto de la clase Ciudad")
        self.nombre = nombre  # variable de la instancia (atributo)
        self.poblacion = poblacion  # variable de la instancia (atributo)


mendoza = Ciudad("Ciudad de Mendoza", 2_000_000)  # se crea un objeto de la clase Ciudad
cordoba = Ciudad("Ciudad de Córdoba", 5_000_000)  # instancia cordoba de la clase Ciudad

print(mendoza.nombre, mendoza.poblacion)
print(cordoba.nombre, cordoba.poblacion)
