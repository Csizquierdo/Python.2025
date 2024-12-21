caja_de_herramientas = [
    "martillo",
    "destornillador",
    "llave inglesa",
    "sierra",
    "tornillo",
]

que_busco = "sierra"

for herramienta in caja_de_herramientas:
    busqueda = True
    while busqueda:
        if herramienta == que_busco:
            print(f"Encontré la herramienta {que_busco}")
            busqueda = False
            break
        else:
            print(f"No quiero usar la herramienta {herramienta}")
            respuesta = input("¿Quieres seguir buscando? (s/n): ")
            if respuesta.lower() in ("s", "si", "sí"):
                print("Continúo con la búsqueda")
                break
            elif respuesta.lower() in ("n", "no"):
                busqueda = False
                print("Fin de la búsqueda")
                break

    if busqueda:
        continue
    break
