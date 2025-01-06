class Empleado:
    def __init__(self, salario) -> None:
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.getter
    def salario(self):
        if self.__salario == 0:
            return "No tiene salario"
        return self.__salario

    @salario.setter
    def salario(self, nuevo_valor):
        if not isinstance(nuevo_valor, int | float):
            raise ValueError("Debes introducir un número")
        if nuevo_valor < 0:
            raise ValueError("El salario no puede ser negativo")

        self.__salario = nuevo_valor

    @salario.deleter
    def salario(self):
        self.__salario = 0


empleado = Empleado(1000)
# print(empleado.get_salario())
print(empleado.salario)
# print(empleado.set_salario(1500))

empleado.salario = 23.3
print(empleado.salario)

del empleado.salario
print(empleado.salario)
