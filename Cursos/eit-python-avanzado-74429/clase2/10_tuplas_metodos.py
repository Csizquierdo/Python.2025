# Métodos de tuplas
serie_fibonacci = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)
print(f"{serie_fibonacci=}")
# count()
# Devuelve el número de veces que aparece un elemento
count = serie_fibonacci.count(1)
print(f"{count=}")
count = serie_fibonacci.count(19)
print(f"{count=}")
# index()
# Devuelve el índice en que aparece el elemento por primera vez
valor_a_buscar = 21
indice = serie_fibonacci.index(valor_a_buscar)
print(f"El valor {valor_a_buscar} está en el índice {indice}")