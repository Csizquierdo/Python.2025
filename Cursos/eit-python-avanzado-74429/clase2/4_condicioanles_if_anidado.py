edad = int(input("Edad: "))
if edad < 13:
    print("eres niño")
else:
    if edad < 18:
        print("eres adolescente")
    else:
        if edad < 65:
            print("eres adulto")
        else:
            if edad < 130:
                print("eres anciano")