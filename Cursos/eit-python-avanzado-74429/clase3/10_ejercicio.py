"""
✨ EJERCICIO ✨

A partir del siguiente diccionario, realizar los ejercicios propuestos:

inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}

1. Se compraron 5 manzanas.
2. Se vendieron 3 naranjas.
3. Se compraron 5 uvas.
4. Solicitar al usuario qué producto está buscando, y, si está disponible,
pedir la cantidad, venderlo y mostrar el inventario. La cantidad no debe superar el stock.

👇 LO NUEVO:
5. Crear un nuevo diccionario con 3 productos, agregarlos al diccionario principal.
6. Calcular el número total de productos en el inventario.
"""

inventario = {"manzanas": 10, "naranjas": 5, "peras": 8}
print(inventario)

# 1. Se compraron 5 manzanas.
inventario["manzanas"] += 5
print(inventario)
# 2. Se vendieron 3 naranjas.
inventario["naranjas"] -= 3
print(inventario)

# 3. Se compraron 5 uvas.
inventario["uvas"] = 5
print(inventario)

# 4. Solicitar al usuario qué producto está buscando, y, si está disponible,
# pedir la cantidad, venderlo y mostrar el inventario. La cantidad no debe superar el stock.

producto = input("¿Qué producto está buscando? ").lower().strip()
if producto in inventario:
    cantidad_a_comprar = int(input("¿Cuántas unidades quiere? "))
    if cantidad_a_comprar > inventario[producto]:
        print("No hay stock suficiente.")
    else:
        inventario[producto] -= cantidad_a_comprar
        print("Venta realizada. Inventario actualizado:", inventario)
else:
    print("No está disponible.")

# 5. Crear un nuevo diccionario con 3 productos, agregarlos al diccionario principal.
mas_productos = {
    "limón": 12,
    "sandía": 3,
    "melón": 7,
}
inventario.update(mas_productos)
print(inventario)

# 6. Calcular el número total de productos en el inventario.
stock_inventario = sum(inventario.values())
print("El stock total del inventario es:", stock_inventario)
