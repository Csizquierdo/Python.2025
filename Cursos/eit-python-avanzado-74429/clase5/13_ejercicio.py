"""
- Crear una clase Persona
  que contenga los atributos:
    - nombre: str
    - edad: str

- Crear 3 instancias de Persona
- Mostrar por pantalla un mensaje elaborado
"""


class Persona:
    def __init__(self, un_nombre, una_edad) -> None:
        self.nombre = un_nombre
        self.edad = una_edad


persona1 = Persona("José", 60)
persona2 = Persona("Lidia", 60)
persona3 = Persona("Roberto", 60)

lista_de_objetos: list[Persona] = [persona1, persona2, persona3]

for persona in lista_de_objetos:
    mensaje = f"El nombre es {persona.nombre} y su edad {persona.edad}"
    print(mensaje)
