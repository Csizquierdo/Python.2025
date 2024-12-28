# Funciones con parámetros opcionales


def datos(a, b, c=0):
    print(a + b + c)


def main():
    datos(1, 2, 3)
    datos(1, 2)
    # datos(1)


main()
