"""
Crear una clase padre que tenga un método de instancia que imprima un saludo.
Luego, una clase hija que herede de la clase padre y que tenga otro método de instancia
que imprima un mensaje diferente al de la clase padre.
Esta clase hija debe conservar el acceso al método de la clase padre
"""


class ClasePadre:
    def saludo(self):
        print("Hola, soy la clase padre.")


class ClaseHija(ClasePadre):
    def mensaje_diferente(self):
        print("Hola, soy la clase hija y tengo un mensaje diferente.")


objeto_clase_padre = ClasePadre()
objeto_clase_padre.saludo()
objeto_clase_hija = ClaseHija()
objeto_clase_hija.saludo()
objeto_clase_hija.mensaje_diferente()
