class Empleado:
    def __init__(self, especialidad, seguro, salario) -> None:
        self.especialidad = especialidad
        self.seguro = seguro
        self.__salario = salario  # atributo privado

    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_valor):
        self.__salario = nuevo_valor


class EmpleadoBonificado(Empleado):
    def __init__(self, especialidad, seguro, salario, bono) -> None:
        super().__init__(especialidad, seguro, salario)
        self.salario = bono


e = Empleado("Desarrollador Junior", "Aseguradora X", 1000)
print(e.especialidad)
print(e.seguro)
# print(e.__salario)
print(e.get_salario())

e.especialidad = "Desarrollador Senior"
print(e.especialidad)

# e.__salario = 2000  # crea un nuevo atributo llamado __salario en el objeto
e.set_salario(2000)
print(e.get_salario())
print(e.__dict__)

eb = EmpleadoBonificado("Analista Funcional", "Aseguradora Y", 2100, 500)
print(eb.__dict__)
