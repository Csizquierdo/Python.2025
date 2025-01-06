class Guitarra:
    def __init__(self, sonido: str) -> None:
        self.sonido = sonido

    def ejecutar(self):
        print(self.sonido)


class GuitarraElectrica(Guitarra):
    def distorsionar(self):
        print("tran tran tran")


guitarra = Guitarra("tin tin tin")
guitarra.ejecutar()
guitarra_electrica = GuitarraElectrica("tin tin tin")
guitarra_electrica.ejecutar()
guitarra_electrica.distorsionar()
