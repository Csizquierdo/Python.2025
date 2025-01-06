class Motor:
    def __init__(self, cilindrada: int) -> None:
        self.cilindrada = cilindrada

    def encender(self):
        print(f"Motor de {self.cilindrada} cilindradas encendido")

    def apagar(self):
        print(f"Motor de {self.cilindrada} cilindradas apagado")


class Auto:
    def __init__(self, marca: str, modelo: str, cilindrada: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(cilindrada)  # Composición: un Auto tiene un Motor

    def arrancar_auto(self):
        print("Arrancando auto...")
        self.motor.encender()

    def detener_auto(self):
        print("Deteniendo auto...")
        self.motor.apagar()


mi_mustang = Auto("Ford", "Mustang", 5000)
mi_mustang.arrancar_auto()
mi_mustang.detener_auto()
