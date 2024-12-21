# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lista_aplanada = []

# for lista in matriz:
#     for n in lista:
#         lista_aplanada.append(n)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_aplanada = [n for lista in matriz for n in lista]


print(lista_aplanada)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
