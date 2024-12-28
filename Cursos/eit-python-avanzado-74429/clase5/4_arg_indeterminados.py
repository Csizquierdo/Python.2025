# Argumentos indetermindados


def sumar(n1, n2, n3):
    print(n1 + n2 + n3)


sumar(20, 5, 6)


def sumar_v2(*numeros):
    # print(type(numeros))
    # print(numeros)
    print(sum(numeros))


sumar_v2(20, 5, 6, 100)


def sumar_v3(*args):
    # print(type(numeros))
    # print(numeros)
    print(sum(args))


sumar_v3(6, 100)


# Crear una función que reciba un arg indeterminado de comidas
# y que imprima cada una de ellas


def comidas(*comidas):
    if len(comidas) == 0:
        print("No hay comidas")
        return
    for comida in comidas:
        if isinstance(comida, str):
            print(comida)


print("*****")
comidas(True, 12, 23.43, "Pizza", "Hamburguesa")
print("*****")
comidas()
