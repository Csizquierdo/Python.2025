print ("*"*50)
import tkinter as tk#<----<-----<----<-----<----<-----<----<-----





from datetime import datetime, date, timedelta
try:
    from PIL import ImageTk, Image# <----<-----<----<-----<----<-----
    '''                                                             importamos la biblioteca PIL solo ImageTk, Image '''
except Exception as error_:
    import pip
    pip.main(['install', 'pillow'])
    from PIL import ImageTk, Image
import random


salidas=[]
def jugar(etiqueta2, etiqueta3,etiqueta_saldo, entrada_apuesta,entrada_numero,boton_jugar):
    global billetera
    if billetera<=1:
        etiqueta2.config(text=f"su saldo es de solo $ {billetera}")
        etiqueta3.config(text="lo esperamos la proxima")
        boton_jugar.place_forget()


    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)

    numero = entrada_numero.get()
    if not numero.isdigit() or int(numero)<2 or int (numero)>12:
        etiqueta2.config(text="Numero no es válido")
        etiqueta3.config(text="Solo digitos de 2 a 12")
        entrada_numero.delete(0,tk.END)
        return
    else:
        numero = int(numero)
    apuesta = entrada_apuesta.get()
    if not apuesta.replace(".","").isdigit() or float(apuesta)<=1 or float (apuesta)>billetera:
        etiqueta2.config(text="Apuesta no es válido")
        etiqueta3.config(text=f"mínimo $1 a máximo {billetera}")
        entrada_apuesta.delete(0,tk.END)
        return
    else:
        apuesta = float(apuesta)
    if (dado_1+dado_2)==numero:
        etiqueta2.config(text=f"Ganaste $ {apuesta*5}")
        billetera += apuesta *5
    else:
        etiqueta2.config(text=f"lo lamento. la proxima ganas")
        billetera -= apuesta
    salidas.append(dado_1+dado_2)
    etiqueta3.config(text=f"salio {dado_1=} + {dado_2=} = {dado_1+dado_2}")
    etiqueta_saldo.config(text=f"su saldo es $ {billetera}")
    return
#######################################################################
def salir():
    for pos in range (2,13):
        print (f"el numero {pos} salio {salidas.count(pos)}")
    print ("adios")
    exit()
#######################################################################
billetera=1000000
def dados():
    ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias
    ventana.title("jugando a los dados")
    ventana.iconbitmap("icono.ico")
    ventana.config(bg="#ffffff")
    ventana.geometry("600x500")
    ventana.resizable(width=False, height=False)
    #-----------------------------------------------------------------------
    etiqueta1 = tk.Label(text=" a jugar a los dados...mucha merd")
    etiqueta1.config( bg="white", fg="blue",font=("Arial", 18))
    etiqueta1.place(x=50, y=300 ,width=500, height=25)
    #-----------------------------------------------------------------------
    etiqueta2 = tk.Label(text="")
    etiqueta2.config( bg="white", fg="black",font=("Arial", 18))
    etiqueta2.place(x=50, y=350 ,width=500, height=25)
    #-----------------------------------------------------------------------
    etiqueta3 = tk.Label(text="")
    etiqueta3.config( bg="#ffffff", fg="#000000",font=("Arial", 18))
    etiqueta3.place(x=50, y=400 ,width=500, height=25)
    #-----------------------------------------------------------------------
    etiqueta_saldo = tk.Label(text=f"su saldo es $ {billetera}")
    etiqueta_saldo.config( bg="white", fg="green",font=("Liberation Serif", 18))
    etiqueta_saldo.place(x=250, y=10 ,width=300, height=25)
    #-----------------------------------------------------------------------
    img = Image.open("dados.jpg")
    img = img.resize((190,190))
    dados =  ImageTk.PhotoImage(img)
    #####################################

    etiqueta_imagen = tk.Label(image=dados)
    etiqueta_imagen.config( bg="blue")
    etiqueta_imagen.place(x=10, y=10 ,width=200, height=200)
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    etiqueta_numero = tk.Label(text="Ingresa tu numero", bg="white", fg="#270F55",font=("Liberation Serif", 12))
    etiqueta_numero.place(x=250, y=75 , width=120, height=25)
    ######################################
    entrada_numero = tk.Entry()
    entrada_numero.place(x=400, y=75 , width=100, height=25)
    #-----------------------------------------------------------------------
    etiqueta_apuesta = tk.Label(text="Ingresa tu apuesta", bg="white", fg="#270F55",font=("Liberation Serif", 12))
    etiqueta_apuesta.place(x=250, y=125 , width=120, height=25)
    ######################################
    entrada_apuesta = tk.Entry()
    entrada_apuesta.place(x=400, y=125 , width=100, height=25)
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    boton_jugar = tk.Button(text="Jugar",bg="#894DFA", command=lambda :jugar(etiqueta2,
                                                                             etiqueta3,
                                                                             etiqueta_saldo,
                                                                             entrada_apuesta,
                                                                             entrada_numero,
                                                                             boton_jugar))
    boton_jugar.place(x=50, y=450, width=100, height=30)


    boton_salir = tk.Button(text="Salir",bg="#894DFA", command=salir)
    boton_salir.place(x=600-50-100, y=450, width=100, height=30)
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    ventana.mainloop()
dados()
