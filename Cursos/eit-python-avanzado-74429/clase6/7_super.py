class ClasePadre:
    def saludo(self):
        print("Hola, soy la clase padre.")


class ClaseHija(ClasePadre):
    def saludo(self):
        print("Hola, soy la clase hija.")
        super().saludo()


objeto_clase_padre = ClasePadre()
objeto_clase_padre.saludo()
objeto_clase_hija = ClaseHija()
objeto_clase_hija.saludo()
