paises: dict[str, dict[str, int]]

paises = {
    "Japón": {"Población": 126476461, "Superficie": 377975},
    "Canadá": {"Población": 38005238, "Superficie": 9984670},
    "Australia": {"Población": 25687041, "Superficie": 7692024},
    "Alemania": {"Población": 83783942, "Superficie": 357386},
    "Brasil": {"Población": 212559417, "Superficie": 8515767},
    "India": {"Población": 1380004385, "Superficie": 3287263},
    "Estados Unidos": {"Población": 331002651, "Superficie": 9833520},
}

for pais, datos in paises.items():
    densidad = datos["Población"] / datos["Superficie"]
    print(f"La densidad de población de {pais} es: {densidad:.2f} personas por km²")

japon = paises["Japón"]
japon_poblacion = japon["Población"]
japon_superficie = japon["Superficie"]
print(japon_poblacion, japon_superficie)

poblacion_india: int = paises["India"]["Población"]
print(poblacion_india)
