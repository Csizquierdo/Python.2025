"""
A partir del siguiente código, identificar cada parte y crear funciones.

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if n1 % n2 == 0:
    print(f"{n1} es múltiplo de {n2}")
else:
    print(f"{n1} no es múltiplo de {n2}")
"""


def ingresar_numeros() -> tuple[int, int]:
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    return n1, n2


def verificar_multiplo(n1: int, n2: int) -> bool:
    if n1 % n2 == 0:
        return True
    else:
        return False


def mostrar_resultado(n1: int, n2: int, es_multiplo: bool) -> None:
    if es_multiplo:
        print(f"{n1} es múltiplo de {n2}")
    else:
        print(f"{n1} no es múltiplo de {n2}")


def main():
    n1, n2 = ingresar_numeros()
    es_multiplo = verificar_multiplo(n1, n2)
    mostrar_resultado(n1, n2, es_multiplo)


main()
