# Métodos de listas

serie_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print(f"{serie_fibonacci=}")

# count e index hacen lo mismo que la tuplas

# append()
# Añade un elemento al final de la lista
calculo_siguiente_valor = serie_fibonacci[-1] + serie_fibonacci[-2]
serie_fibonacci.append(calculo_siguiente_valor)
print(f"{serie_fibonacci=}")

# extend()
# Añade los elementos de una lista a otra lista existente, al final de la primera
mas_numeros = [377, 610, 987, 1597]
serie_fibonacci.extend(mas_numeros)
print(f"{serie_fibonacci=}")

# insert()
# Añade un elemento en la posición indicada
indice = 0
serie_fibonacci.insert(indice, "inicio")
print(serie_fibonacci)

# remove()
# Elimina el primer elemento cuyo valor coincida con lo que pasamos
valor_a_eliminar = "inicio"
serie_fibonacci.remove(valor_a_eliminar)
if valor_a_eliminar in serie_fibonacci:
    serie_fibonacci.remove(valor_a_eliminar)
print(serie_fibonacci)

# pop()
# Elimina el último elemento y lo devuelve
# serie_fibonacci.pop()
elemento_eliminado = serie_fibonacci.pop()
print(serie_fibonacci, f"Elemento eliminado {elemento_eliminado}")

# pop(indice)
indice = 0
elemento_eliminado = serie_fibonacci.pop(indice)
print(serie_fibonacci, f"Elemento eliminado {elemento_eliminado}")

# sort()
letras = ["z", "a", "b", "j", "c"]
letras.sort()
print(letras)

# reverse()
letras.reverse()
print(letras)

# clear()
serie_fibonacci.clear()
# serie_fibonacci = []
print(serie_fibonacci)
