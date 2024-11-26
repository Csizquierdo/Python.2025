"""
Consigna: mostrar por la terminal el mensaje:

"La función upper() sirve para poner en mayúsculas las cadenas"

La subcadena 'upper()' debe ser guardada en una variable.
Para el primer print, usar las 3 formas concatenación, +, coma, f-strings
"""

comando = "upper()"
print("La función " + comando + " sirve para poner en mayúsculas las cadenas")
print("La función", comando, "sirve para poner en mayúsculas las cadenas")
print(f"La función {comando} sirve para poner en mayúsculas las cadenas")

#  Esta última es la que se usa cada vez menos:
print("La función {} sirve para poner en mayúsculas las cadenas".format(comando))
