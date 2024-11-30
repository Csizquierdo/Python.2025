edad = int(input("Edad: "))


if edad < 0 or edad >= 130:
   print("Numero invalido")
elif edad < 13:
    print("eres niño")
elif edad < 18:
        print("eres adolescente")
elif edad < 65:
        print("eres adulto")
elif edad < 130:
        print("eres anciano")