"""
Crear una tupla que represente un cajón de verduras
Crear otra tupla que represente un cajón de frutas
Crear una tupla llamada camion, que contenga los dos cajones anteriores
Mostrar los datos
"""

cajon_verduras = ("morron","tomate","cebolla")
cajon_frutas = ("sandia","manzana","banana")

#Cargamos camion 1 
camion1 = (cajon_frutas, cajon_verduras)
print (camion1)

#Descargamo camion 1
cajon_frutas, cajon_verduras = camion1
print("Cajon de verduras:", cajon_verduras)
print("Cajon de frutas: ", cajon_frutas)

#Cargamos camion 2
camion2 = cajon_verduras + cajon_frutas
print("Camion 2", camion2)

# Cargamos camión 3
camion3 = (*cajon_frutas, *cajon_verduras)
print("Camión 3", camion3)