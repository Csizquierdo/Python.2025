# Métodos de conjuntos para operaciones de conjuntos

# union(set)
# Devuelve un nuevo conjunto con los elementos de ambos conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
union_ab = conjunto_a.union(conjunto_b)
print(f"{union_ab=}")
# Con símbolo |
union_ab = conjunto_a | conjunto_b
print(f"{union_ab=}")

# intersection(set)
# Devuelve un nuevo conjunto con los elementos comunes en ambos conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
interseccion_ab = conjunto_a.intersection(conjunto_b)
print(f"{interseccion_ab=}")
# Con símbolo &
interseccion_ab = conjunto_a & conjunto_b
print(f"{interseccion_ab=}")

# difference(set)
# Devuelve un nuevo conjunto con los elementos del primer conjunto
# que no están en el segundo
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
diferencia_ab = conjunto_a.difference(conjunto_b)
print(f"{diferencia_ab=}")
# Con símbolo -
diferencia_ab = conjunto_a - conjunto_b
print(f"{diferencia_ab=}")

# symmetric_difference(set)
# Devuelve un nuevo conjunto con los elementos que nos son compartidos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(f"{diferencia_simetrica=}")
# Con símbolo ^
diferencia_simetrica = conjunto_a ^ conjunto_b
print(f"{diferencia_simetrica=}")

# issuperset(set)
# Devuelve True si el conjunto es un superconjunto del otro
abecedario = {"a", "b", "c", "d", "e"}
vocales = {"a", "e"}

if abecedario.issuperset(vocales):
    print("Las vocales están incluidas en el abecedario")

# update(set)
# Actualiza el conjunto con los elementos de otro conjunto
abecedario.update(vocales)
abecedario.update({"f", "g"})
print(f"{abecedario=}")
