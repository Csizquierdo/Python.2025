class Especie:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Animal:
    def __init__(self, nombre: str, especie: Especie, sonido: str):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"{self.nombre} hace: {self.sonido}")


# Crear dos  instancias de la clase Especie
canis = Especie("Canis")
felis = Especie("Felis")

# Crear dos instancias de la clase Animal
perro = Animal("Fido", canis, "Guau")
gato = Animal("Garfield", felis, "Miau")

print(perro.nombre)
print(perro.sonido)
print(perro.especie)
perro.hacer_sonido()
