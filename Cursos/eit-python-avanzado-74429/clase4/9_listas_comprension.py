# numeros = [1, 2, 3, 4, 5]
# cuadrados = []

# for n in numeros:
#     cuadrados.append(n**2)


numeros = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in numeros]

print(cuadrados)  # [1, 4, 9, 16, 25]
