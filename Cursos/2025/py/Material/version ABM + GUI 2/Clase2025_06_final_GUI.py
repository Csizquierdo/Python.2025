#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import math
import datetime
#######################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
    limpiar()
#######################################################################################################
limpiar()
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║    ╔═══════╗            ╦                                   ╦   ╔═══╦═══╗   ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗         ║       ║       ║
║    ║            ║       ║    ║       ║    ║                 ║       ║       ║
║    ║            ║       ║    ║       ║    ║          ╔╗     ║       ║       ║
║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝     ╩       ╩       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣\033[0;m
║                                                                             ║
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
║                                                                             ║
║  ╔═════╗   ╔╗       ╔╗   ╔═════╗    ╔╗      ╦                               ║
║ ╔╝     ╚╗   ║       ║   ╔╝     ╚╗   ║╚╗     ║                               ║
║ ║       ║   ╚╗     ╔╝   ║       ║   ║ ╚╗    ║                               ║
║ ║       ║    ║     ║    ║       ║   ║  ╚╗   ║                               ║
║ ╠═══════╣    ╚╗   ╔╝    ╠═══════╣   ║   ╚╗  ║  ╠═════╣                      ║
║ ║       ║     ║   ║     ║       ║   ║    ╚╗ ║                               ║
║ ║       ║     ╚╗ ╔╝     ║       ║   ║     ╚╗║                               ║
║ ╩       ╩      ╚═╝      ╩       ╩   ╩      ╚╝                               ║
║                                                                             ║
║                                                                             ║
║                             ╔═══════╗   ╔═════╗  ╔══════╗    ╔═════╗        ║
║                                    ╔╝  ╔╝     ╚╗ ║      ╚╗  ╔╝     ╚╗       ║
║                                   ╔╝   ║       ║ ║       ║  ║       ║       ║
║                                  ╔╝    ║       ║ ║       ║  ║       ║       ║
║                               ╔══╝     ╠═══════╣ ║       ║  ║       ║       ║
║                              ╔╝        ║       ║ ║       ║  ║       ║       ║
║                             ╔╝         ║       ║ ║      ╔╝  ╚╗     ╔╝       ║
║                             ╚═══════╝  ╩       ╩ ╚══════╝    ╚═════╝        ║
║                                                                             ║
║                                                                             ║
║      ╔═════╗       ╔═════╗       ╦           ╦   ╔═══╦═══╗   ╔═══════╗      ║
║     ╔╝     ╚╗     ╔╝     ╚╗      ║           ║       ║       ║              ║
║     ║       ║     ║       ║      ║           ║       ║       ║              ║
║     ╚╗            ║       ║      ║           ║       ║       ║              ║
║      ╚══════╗     ║       ║      ║           ║       ║       ╠═════╣        ║
║             ║     ║       ║      ║           ║       ║       ║              ║
║     ╚╗     ╔╝     ╚╗    ╔╦╝      ║           ║       ║       ║              ║
║      ╚═════╝       ╚════╝╚═╝     ╚═══════╝   ╩       ╩       ╚═══════╝      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""");
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os
import time

nombre=""
Telefono= ""
email=  ""
cursos=  ""
DDBB_nombre = "cursos"
DDBB_tabla = "curso_2025"
datos = {"Nombre": {"Telefono": "", "EMail": "", "Cursos": ""}}
cargado = False
llamado_flag = ""
proy = ()
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

def make_windows():
    global ventana,alumnos_cursos,marco,entry_nombre,entry_celular,entry_email,etiq_todos_los_cursos,etiq_subtitulo,total_cursos,tabla,bot_aceptar,bot_cargar,bot_agregar,bot_cancelar,bot_cargar,bot_modificar,bot_borrar,bot_salir 
    
    ventana = tk.Tk()
    ventana.iconbitmap("icono.ico")
    ventana.config(width=640, height=550, bg="#E5E5E5")
    ventana.title("Ed.IT")

    ventana.resizable(False, False)

    etiq_titulo = tk.Label(text="Agenda 2025:", bg="#E5E5E5", fg="blue", font=("Helvetica", 18))
    etiq_titulo.place(x=200, y=10, width=400, height=30)

    etiq_subtitulo = tk.Label(text="", bg="#E5E5E5", fg="blue", font=("Helvetica", 14))
    etiq_subtitulo.place(x=200, y=40, width=400, height=30)

    img_original = Image.open("IT.png")
    img_resize = img_original.resize((150, 50))
    img_resize_tkinter = ImageTk.PhotoImage(img_resize)
    et_imagen = tk.Label(image=img_resize_tkinter)
    et_imagen.place(x=1, y=1, width=150, height=50)

    ##############################################################################################
    marco = tk.Frame(ventana,
                                 relief=tk.RAISED,  # Estilo del borde: RAISED, SUNKEN, FLAT, GROOVE, RIDGE
                                 borderwidth=2,     # Ancho del borde
                                 bg="#E5E5E5"       # Color de fondo
                    )
    marco.place(x=20, y=75, width=600, height=130)
    marco.place_forget()

    etiq_nombre = tk.Label(marco, text="Ingrese el nombre:", bg="#E5E5E5")
    etiq_nombre.place(x=10, y=15, width=150, height=30)
    entry_nombre = tk.Entry(marco)
    entry_nombre.place(x=170, y=15, width=150, height=20)
    etiq_celular = tk.Label(marco, text="Ingrese el Telefono:", bg="#E5E5E5")
    etiq_celular.place(x=10, y=40, width=150, height=30)
    entry_celular = tk.Entry(marco)
    entry_celular.place(x=170, y=40, width=150, height=20)
    etiq_email = tk.Label(marco, text="Ingrese el EMail:", bg="#E5E5E5")
    etiq_email.place(x=10, y=65, width=150, height=30)
    entry_email = tk.Entry(marco)
    entry_email.place(x=170, y=65, width=150, height=20)
    etiq_todos_los_cursos = tk.Label(marco, text="Todos los Cursos:", bg="#E5E5E5")
    etiq_todos_los_cursos.place(x=10, y=90, width=150, height=30)
    alumnos_cursos = ttk.Combobox(marco,
                state="readonly",
                values=[]
            )
    alumnos_cursos.place(x=170, y=90, width=150, height=20)
    etiq_total_cursos = tk.Label(marco, text="Cambiar Cursos:", bg="#E5E5E5")
    etiq_total_cursos.place(x=400,y=65,width=180, height=30)
    total_cursos = ttk.Combobox(marco, state="readonly",
                values=["Python", "C", "C++", "Java","c#","vb.net","javascript","assembly","php","perl","ruby","swift","r"]
            )
    total_cursos.place(x=400,y=90,width=180, height=20)
    total_cursos.bind("<<ComboboxSelected>>", seleccionar_curso)
    #--------------------------------------------------------------------------------------------
    tabla = ttk.Treeview(ventana, columns=("Telefono", "EMail", "Cursos"))
    tabla.heading("#0", text="Nombre", anchor=tk.CENTER)
    tabla.heading("#1", text="Telefono", anchor=tk.CENTER)
    tabla.heading("#2", text="EMail", anchor=tk.CENTER)
    tabla.heading("#3", text="Cursos", anchor=tk.CENTER)
    tabla.column("#0", minwidth=50, width=170, stretch=False)
    tabla.column("#1", minwidth=50, width=150, stretch=False)
    tabla.column("#2", minwidth=50, width=150, stretch=False)
    tabla.column("#3", minwidth=50, width=170, stretch=False)
    tabla.place(x=20, y=75, width=600, height=375)
    #--------------------------------------------------------------------------------------------
    style = ttk.Style()
    style.theme_use("classic")
    style.map("C.TButton",
                    foreground=[('!active', 'black'), ('pressed', 'black'), ('active', 'black')],
                    background=[('!active', '#E5E5E5'), ('pressed', 'lightblue'), ('active', 'grey75')]
              )
    bot_aceptar = ttk.Button(marco, text="Aceptar", command=aceptar,style="C.TButton")
    bot_aceptar.place(x=400,y=25,width=80, height=40)

    bot_cancelar = ttk.Button(marco, text="Cancelar", style="C.TButton" , command=cancelar)
    bot_cancelar.place(x=500,y=25,width=80, height=40)
    #----------------------------------------------------
    bot_cargar = ttk.Button(ventana, text="Cargar", style="C.TButton", command=lambda: cargar(tabla))
    bot_cargar.place(x=100, y=475, width=80, height=40)

    bot_agregar = ttk.Button(ventana, text="Agregar", command=lambda:subir_de_tabla_a_marco("add"), style="C.TButton")
    bot_agregar.place(x=180, y=475, width=80, height=40)

    bot_modificar = ttk.Button(ventana, text="Modificar", command=lambda:subir_de_tabla_a_marco("modificar"), style="C.TButton")
    bot_modificar.place(x=260, y=475, width=80, height=40)

    bot_borrar = ttk.Button(ventana, text="Borrar", command=lambda:subir_de_tabla_a_marco("borrar"), style="C.TButton")
    bot_borrar.place(x=340, y=475, width=80, height=40)

    bot_salir = ttk.Button(ventana, text="Salir", command=ventana.quit, style="C.TButton")
    bot_salir.place(x=420, y=475, width=80, height=40)

    ventana.mainloop()


##############################################################################################
def cargar(tabla):
    global cargado
    read_data()
    if cargado:
        vaciar_contenido_tabla(tabla)
    cargado = True
    for Indice, [nombre, valores] in enumerate(datos.items()):
        tabla.insert('', tk.END, iid=Indice, text=nombre, values=(datos[nombre]["Telefono"],
                                                                   datos[nombre]["EMail"],
                                                                   datos[nombre]["Cursos"]))
##############################################################################################
def vaciar_contenido_tabla(tabla):
    tabla.delete(*tabla.get_children())
    ventana.update()
##############################################################################################
def carga_entries(datos):
    entry_nombre .delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_email  .delete(0, tk.END)
    alumnos_cursos["values"]=["",]
    if datos[0].isdigit():
        entry_nombre. insert(0,tabla.item(tabla.selection())['text'])
        entry_celular.insert(0,tabla.item(tabla.selection())["values"][0])
        entry_email.  insert(0,tabla.item(tabla.selection())["values"][1])
        alumnos_cursos["values"]=tabla.item(tabla.selection())["values"][2]

##############################################################################################
def subir_de_tabla_a_marco(boton_origen):
    global llamado_flag   
    llamado_flag = boton_origen
    if cargado is False:
        result = messagebox.showerror("Error","Primero se debe cargar los datos")
        return
    id_seleccionado= tabla.selection()#metodo selection[0] devuenve una tupla con la seleccion
    if len(id_seleccionado)==0 and boton_origen!="add":
        result = messagebox.showinfo("Error","debe seleccionar un item\nCliquee sobre el")
        marco_superior(False)
        return
    elif boton_origen=="add":
        id_seleccionado=("",)
    marco_superior(True)
    carga_entries(id_seleccionado)
    return

##############################################################################################
def cancelar():
    marco_superior(False)
##############################################################################################
def marco_superior(estado):
    if not estado:
        marco.place_forget()
        bot_cargar.place(x=100, y=475, width=80, height=40)
        bot_agregar.place(x=180, y=475, width=80, height=40)
        bot_modificar.place(x=260, y=475, width=80, height=40)
        bot_borrar.place(x=340, y=475, width=80, height=40)
        bot_salir.place(x=420, y=475, width=80, height=40)
        tabla.place(x=20, y=75, width=600, height=375)
    else:
        marco.place(x=20, y=75, width=600, height=130)
        bot_cargar.place_forget()
        bot_agregar.place_forget()
        bot_modificar.place_forget()
        bot_borrar.place_forget()
        tabla.place(x=20, y=250, width=600, height=200)
    alumnos_cursos.set("")
    bot_salir.place(x=420, y=475, width=80, height=40)
##############################################################################################
def validar():
    nombre = entry_nombre.get().upper()
    if not nombre  :# or nombre in datos.keys()
        messagebox.showinfo("Error", "Debe ingresar un nombre valido")
        entry_nombre.delete(0, tk.END)
        return

    if llamado_flag == "add"   and nombre in datos.keys():
        messagebox.showinfo("Error", "Usted esta agregando:\nNombre duplicado, cambielo o ingrese a modificar")
        entry_nombre.delete(0, tk.END)
        return

    Telefono = entry_celular.get()
    if not Telefono:
        messagebox.showinfo("Error", "Debe ingresar un Telefono valido")
        entry_celular.delete(0, tk.END)
        return
    email=entry_email.get()
    patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if email=="" and not re.match(patron_email, email):
        messagebox.showinfo("Error","Debe ingresar un email valido")
        entry_email.delete(0,tk.END)
        return
    alumnos_str_cursos= ",".join(alumnos_cursos["values"])

    if len(alumnos_str_cursos)>0 and alumnos_str_cursos[0]==",":
        alumnos_str_cursos=alumnos_str_cursos[1:]
    return (nombre,Telefono,email,alumnos_str_cursos)


# ~ ################################################################################
# ~ def validar_Telefono(numero):
    # ~ patron_telefono = r'^\+\d{1,3}\s\d{1,14}(\s\d{1,13})?$'
    # ~ return re.match(patron_telefono, numero)


##############################################################################################
def aceptar():
    validado = validar() 
    if not isinstance(validado, (list,tuple)):
        return
    nombre,Telefono,email,alumnos_str_cursos = validado
    salida = ""
    match llamado_flag:
        case "borrar":
            query = f"""DELETE FROM {DDBB_tabla} WHERE Nombre=?;"""
            salida = (nombre,)
        case "modificar":
            query = f"UPDATE {DDBB_tabla} SET Telefono = ?, EMail = ?, Cursos = ? WHERE Nombre = ?;"
            salida = (Telefono,email,alumnos_str_cursos,nombre)
        case "add":
            query = f"""INSERT INTO {DDBB_tabla} ("Nombre", "Telefono", "EMail", "Cursos") VALUES (?,?,?,?);"""
            salida = (nombre,Telefono,email,alumnos_str_cursos)
        case _:
            return
    abm(query,salida)
    datos[nombre]= {"Telefono":Telefono,"EMail":email, "Cursos": alumnos_str_cursos}
    cargado = True
    cargar(tabla)
    marco_superior(False)

################################################################################
def seleccionar_curso(event):
    item_seleccionado = total_cursos.get().upper()
    alumnos_list_cursos=[cada_curso for cada_curso in alumnos_cursos["values"] if cada_curso !=""]
    if item_seleccionado:
        if item_seleccionado not in alumnos_cursos["values"]:
            alumnos_list_cursos.append(item_seleccionado)
            salida = f"Si aceptas agregaras el curso {item_seleccionado} a tu lista"
            messagebox.showinfo("Éxito", f"{salida}")
        else:
            alumnos_list_cursos.remove(item_seleccionado)
            item_seleccionado=""
            salida = f"Si aceptas eliminaras el curso {item_seleccionado} de tu lista"
            messagebox.showwarning("Advertencia", f"{salida}")
        etiq_subtitulo.config( text= f"{salida}")
        alumnos_cursos["values"] = alumnos_list_cursos
        alumnos_cursos.set(item_seleccionado)
    else:
        messagebox.showerror("Error", "El campo de entrada está vacío.")
    total_cursos.set('')
    return
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

def conectar_base_de_datos():
    connection = sqlite3.connect(f'{DDBB_nombre}.db')
    return connection, connection.cursor()
##############################################################################################
def close_connection(cursor, connection):
    cursor.close()
    connection.close()
##############################################################################################
def read_data():
    global datos
    datos = {}
    connection, cursor = conectar_base_de_datos()
    cursor.execute(f'SELECT * FROM {DDBB_tabla} ')#where estado = 'ACTIVO'
    rows = cursor.fetchall()
    for row in rows:
        # ~ id_ = row[0]
        # ~ Nombre = row[1]
        # ~ Telefono = row[2]
        # ~ Email = row[3]
        # ~ Cursos = row[4]
        id_,Nombre, Telefono, Email, Cursos = row
        datos[Nombre.upper()] = {
                                    'Telefono': Telefono.upper(),
                                    'EMail': Email.upper(),
                                    'Cursos': Cursos.upper()
                                }
    close_connection(cursor, connection)
##############################################################################################
def abm (query,salida):
    try:
        connection, cursor = conectar_base_de_datos()
        cursor.execute(query,salida)
        connection.commit()
        cant_datos_modificados = cursor.rowcount
        if cant_datos_modificados==0:
             messagebox.showwarning("Error",f"la base de datos no se actualizo",icon="warning")
        else:
            etiq_subtitulo.config( text= f"{cant_datos_modificados} registro actualizados")
    except:
        messagebox.showwarning("Error",f"No se pudo acceder a la base de datos",icon="warning")
    finally:
        close_connection(cursor, connection)
##############################################################################################
if  not os.path.isfile(f"{DDBB_nombre}.db"):
    print ("no hay base de datos disponible.")
    
    DDBB_nombre = "cursos"
    DDBB_tabla = "curso_2025"
    DDBB_campos = {
                            "id"        :"INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL",
                            "Nombre"    :"VARCHAR(100) NOT NULL UNIQUE",
                            "Telefono"  :"VARCHAR(20) NOT NULL",
                            "Email"     :"VARCHAR(75) NOT NULL",
                            "Cursos"    :"VARCHAR(255) NOT NULL"
                            } 
    datos=[(5, 'ANA', '54 9 11 98765432', 'Ana@gmail.com', 'C,PYTHON,ASSEMBLY'), (6, 'PEPE', '54 9 11 23455432', 'PEPE@GMAIL.COM', 'C++,JAVA,VB.NET'), (7, 'ANDREA', '54 9 11 11223344', 'Andrea@gmail.com', 'PYTHON,C,PYTHON'), (8, 'LUIS', '54 9 11 12345678', 'Luis@gmail.com', 'C++,C,PYTHON'), (9, 'PEDRO', '54 9 11 88455432', 'Pedro@gmail.com', 'JAVA,C,PYTHON'), (10, 'ADRIANO', '54 9 11 88223344', 'ANDRIANO@GMAIL.COM', 'JAVA,PYTHON'), (11, 'ANALIA', '54 9 11 88345678', 'ANALIA@GMAIL.COM', 'JAVA,C,PERL,PHP,R,PYTHON,ASSEMBLY'), (12, 'JUAN', '54 9 11 99887766', 'JUANA@GMAIL.COM', 'C,ASSEMBLY,PYTHON'), (13, 'LUCAS', '54 9 11 42375675', 'LUCAS@LUQUITAS.COM', 'PYTHON,R,JULIA,PERL,PERL,ASSEMBLY,PHP')]
    coneccion, cursor = conectar_base_de_datos()
    columnas = ""
    for clave, valor in  DDBB_campos.items():
        columnas += f""" {clave} { valor},"""
    # ~ if base_de_datos == "M":
         # ~ columnas = columnas.replace("INTEGER", "INT").replace("AUTOINCREMENT", "AUTO_INCREMENT").replace("?", "%s")
    columnas=columnas[:-1]
    print (f"{columnas=}")
    query= (f"""CREATE TABLE IF NOT EXISTS {DDBB_tabla} ({columnas});""")
    cursor.execute(query)

    # Guardar y cerrar
    coneccion.commit()
    # Insertar los datos
    cantidad_columnas = len(DDBB_campos.keys())
    marcadores = ','.join(['?'] * cantidad_columnas)
    print (f"{marcadores=}")
    query = f"INSERT INTO {DDBB_tabla} VALUES ({marcadores});"
    print (f"""
    {query=}
    {datos=}
    """)
    cursor.executemany(query, datos)

    # Guardar y cerrar
    coneccion.commit()
    coneccion.close()

read_data()
make_windows()




























