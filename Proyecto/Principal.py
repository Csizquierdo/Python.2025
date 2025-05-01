
print('''
╔════════════════════════════╗
║                            ║
║ Ingresar sistema deseado:  ║
║                            ║
║     A- Ventas              ║
║     B- RRHH                ║
║     C- Stock               ║
║     Z- Salir               ║
║                            ║
╚════════════════════════════╝
''')

principal = {
    "A": "Ventas",
    "B": "RRHH",
    "C": "Stock",  
}

sector = input ("Ingrese opcion")

print("BBBBBB")

while sector != "Z":
    match sector:
        case "A":
            print("caso A")
            #Principal[]
        case "B":
            print("caso B")
            #Principal = {}
        case "C":
            print("caso C")
            #Principal = {}
