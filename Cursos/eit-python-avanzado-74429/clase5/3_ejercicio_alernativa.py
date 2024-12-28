"""
Crear una función que tenga como parámetros:
        - nombre
        - fecha de nacimiento (opcional)

Pedir al usuario que ingrese los datos y mostrarlos
Si no ingresa fecha de nacimiento, mostrar el mensaje "no ingresó fecha de nacimiento"

Código:
nombre = input("Ingrese su nombre: ")
fecha_nacimiento = input("Ingrese su fecha de nacimiento (opcional): ")
if fecha_nacimiento == "":
                print("No ingresó fecha de nacimiento")
else:
                print("Nombre:", nombre)
                print("Fecha de nacimiento:", fecha_nacimiento)
"""

from datetime import datetime


def ingresar_datos() -> tuple:
    nombre = input("Ingrese su nombre: ")
    fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
    fecha_nacimiento = (
        datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y") if fecha_nacimiento_str else None
    )
    return nombre, fecha_nacimiento


def mostrar_datos(nombre: str, fecha_nacimiento: datetime | None) -> None:
    if fecha_nacimiento:
        print("Nombre:", nombre)
        print("Fecha de nacimiento:", fecha_nacimiento.strftime("%d/%m/%Y"))
    else:
        print("No ingresó fecha de nacimiento")


def main():
    nombre, fecha_nacimiento = ingresar_datos()
    mostrar_datos(nombre, fecha_nacimiento)


main()
