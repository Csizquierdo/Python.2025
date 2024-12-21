nombres = ["Hugo", "Paco", "Luis"]
edades = [30, 25, 27]

# gente = []
# # gente: list = []
# # gente: list[tuple] = []
gente: list[tuple[str, int]] = []

# for nombre in nombres:
#     for edad in edades:
#         gente.append((nombre, edad))


gente = [(nombre, edad) for nombre in nombres for edad in edades]

print(gente)
