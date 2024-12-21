def elevar_cuadrado(numero: int | float) -> int | float:
    numero = numero**2
    return numero


numero = 4
cuadrado = elevar_cuadrado(numero)
print(f"El cuadrado de {numero} es {cuadrado}")


def concatenar_string(cadena: str) -> str:
    cadena = cadena + "!"
    return cadena


string = "Hola"
concatenado = concatenar_string(string)
print(string)
print(concatenado)


# Colecciones


def funcion_lista(lista: list) -> list:
    lista.append("Python")
    return lista


lista_original = ["C++", "JavaScript"]
# resultado = funcion_lista(lista_original)
resultado = funcion_lista(lista_original.copy())
print(lista_original, id(lista_original))
print(resultado, id(resultado))
