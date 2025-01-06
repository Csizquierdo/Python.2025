class Corredor:
    def correr(self):
        print("Corriendo")


class Nadador:
    def nadar(self):
        print("Nadando")


class Atleta(Corredor, Nadador):
    def saltar(self):
        print("Saltando")


atleta = Atleta()
atleta.saltar()
atleta.correr()
atleta.nadar()
