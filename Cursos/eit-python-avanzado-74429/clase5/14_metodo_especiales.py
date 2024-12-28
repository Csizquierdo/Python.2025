class Persona:
    def __init__(self, un_nombre, una_edad) -> None:
        self.nombre = un_nombre
        self.edad = una_edad

    def __str__(self) -> str:
        return f"El nombre es {self.nombre} y su edad {self.edad}"


persona1 = Persona("José", 60)
persona2 = Persona("Lidia", 60)
persona3 = Persona("Roberto", 60)


# print(persona1)
# print(persona2)
# print(persona3)
