class Empleado:
    def __init__(self, salario) -> None:
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_valor):
        self.__salario = nuevo_valor


empleado = Empleado(1000)
# print(empleado.get_salario())
print(empleado.salario)
# print(empleado.set_salario(1500))

empleado.salario = 1500
print(empleado.salario)
