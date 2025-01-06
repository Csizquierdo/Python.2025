class Vehiculo:
    def arrancar(self):
        print("El vehículo ha arrancado")


class Auto(Vehiculo):
    def tocar_bocina(self):
        print("Tocando bocina...")


class MovimientosMarinosMixin:
    """Un mixin es una clase que no está destinada a ser instanciada"""

    def navegar(self):
        print("Navegando en el agua...")


class Lancha(Vehiculo, MovimientosMarinosMixin):
    pass


auto = Auto()
auto.arrancar()
auto.tocar_bocina()

lancha = Lancha()
lancha.arrancar()
lancha.navegar()
