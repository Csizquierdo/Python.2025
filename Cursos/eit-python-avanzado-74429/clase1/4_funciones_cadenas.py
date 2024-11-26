cadena = " esta es una prueba con Pithon 🔥 🔥"
#         0123456789
#                  10
#                   11
print("Longitud de la cadena:", len(cadena))
print("Representación:", type(cadena))

print(cadena.upper())
print(cadena.lower())
print(cadena.strip())
print(cadena.strip().capitalize())
print(cadena.count("🔥"))
print(cadena.title())
print("0123456789".isdecimal())
print("0123456789aaaa".isdecimal())
print("nombre".isalpha())
print(cadena.startswith(" es"))
print(cadena.replace("e", "3"))
print(cadena.replace("Pithon", "Python"))
print(cadena.find("t"))
print(cadena.find("t", 4))
