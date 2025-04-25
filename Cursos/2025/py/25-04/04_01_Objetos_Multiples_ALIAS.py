from Estructura import *
import datetime
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aquí las practicas hechas
    pass
limpiar();

datoT=  [
            ['Pedro', 'Pepe', 'Ana', 'Juan', 'Manuel'],
            [1234, 5432, 2323, 8787, 9000],
            [True, False, True, False, True]
        ]
print("------------------------------------")
print ("Matriz :",datoT)

print("------------------------------------")
print("\t\t\tasigno listas desde la matriz")

Nombres = datoT[0]
Telefonos = datoT[1]
Datosbool= datoT[2]

print ("Nombres:",Nombres )
print ("Telefonos: ",Telefonos )
print ("Datosbool:", Datosbool)
print("------------------------------------")
print("\t\t\tAgrego datos en listas")
print (type(Nombres))
Nombres.append("Ariel")

Telefonos.append(65748)
Datosbool.append(True)
print("------------------------------------")
print ("Matriz :",datoT)
datoT[2][2]=False
print("------------------------------------")
print ("Matriz :",datoT)


pausa();limpiar();
#################################################################
datos = [
            ["Pedro"    ,1234       ,True   ],
            ["Pepe"     ,5432       ,False  ],
            ["Ana"      ,2323       ,True   ],
            ["Juan"     ,8787       ,False  ],
            ["Manuel"   ,9000       ,True   ]
        ]

print("\t\t\tAgrego datos en listas")


print("------------------------------------")
print("\t\t\tTranspongo la matriz")
result = map(list, zip(*datos))
datoS=[]
for r in result:
    print(r)
    datoS.append(r)
print ("Matriz :",datoS)
print("------------------------------------")
print("\t\t\tasigno listas desde la matriz")
Nombres = datoS[0]
Telefonos = datoS[1]
Datosbool= datoS[2]

print ("Nombres:",Nombres )
print ("Telefonos: ",Telefonos )
print ("Datosbool:", Datosbool)
print("------------------------------------")
print("\t\t\tAgrego datos en listas")
print (type(Nombres))
Nombres.append("Ariel")
Telefonos.append(65748)
Datosbool.append(True)

print ("Matriz :",datoS)
print("------------------------------------")
print("\t\t\tvuelvo a transponer la matriz")
datos=[]
result = map(list, zip(*datoS))
datoS=[]
for r in result:
    print(r)
    datos.append(r)
print ("Matriz :",datos)


print("------------------------------------")
pausa();limpiar();
#################################################################
datos={
    "Pedro":"",
    "Pepe": {
            "Telefono":['222']
            },
    "Juan": {
            "Telefono":
                        {
                        "Casa":['222'],
                        "Trabajo":['222']
                        },
             "Direccion": "xx555"
            },
    "Juana":{
            "Telefono":
                        {
                        "Casa":['222'],
                        "Trabajo":
                                    {
                                    "fijo":['222'],
                                    "celular":['222']
                                    }
                        },
            "Direccion":
                        {
                        "Casa":"xx789",
                        "Trabajo":"xx999"
                        },
            "dni":"12345678"
            },
    "Andrea":
            {"Telefono":
                        {
                        "Casa":['222'],
                        "Trabajo":['222']
                        },
            "Direccion": "xx123"
            },
    "Andres":
            {
            "Telefono":
                        {
                        "Casa":['222'],
                        "Trabajo":['222']
                        },
             "Direccion": "xx123"
            },
    "Martin":
                {
                "Telefono":
                            {
                            "Casa":['222'],
                            "Trabajo":['222']
                            },
                "Direccion": "xx123"
                },
    "Martina":
                {
                "Telefono":
                            {"Casa":['222'],
                            "Trabajo":['222']
                            },
                "Direccion": "xx123"
                },
    "Joaquin":
                {
                "Telefono":
                            {
                            "Casa":['222'],
                            "Trabajo":['222']
                            },
                "Direccion": "xx123"
                },
    "Julia":
                {
                "Telefono":
                            {"Casa":['222','3443'],
                            "Trabajo":['222']
                            },
                "Direccion": "xx123"},
    "Julio":
                {
                "Telefono":
                            {"Casa":['222'],
                            "Trabajo":['222']
                            },
                "Direccion": "xx123"
                },
    "Facundo":
                {
                "Telefono":123
                }
    }
claves = datos.keys()
print("claves:",claves)
valores = datos.values()


print("dato",datos["Julia"]["Telefono"]["Casa"])
elemento = datos["Julia"]["Telefono"]["Casa"]
print ("elemento",elemento)
elemento[0]= "98777899887789"
print ("elemento",elemento)

print("dato",datos["Julia"]["Telefono"]["Casa"])
datos["Julia"]["Telefono"]["Casa"]= "98777899887789"
print("dato",datos["Julia"]["Telefono"]["Casa"])
"""
for clave_u in datos:

    print (clave_u)
    try:
        print(datos[clave_u]["Telefono"]["Casa"])
    except:
        print ("sin datos")
"""

