'''
Autor: Daniel Sanchez
Código: 202180615-2724
Fecha: 24 de Junio del 2022
'''

from tkinter import *
from tkinter import ttk

def salir():
    raiz.destroy()
    
def borrar():
    nombreACombo.set("")
    notaETb.delete(0, END)
    notaT1Tb.delete(0, END)
    notaT2Tb.delete(0, END)
    notaT3Tb.delete(0, END)
    varDefinitiva.set("")
    varMensaje.set("")

def principal():
    asignatura = nombreACombo.get()
    notaExamen = float(notaETb.get())
    notaTarea1 = float(notaT1Tb.get())
    notaTarea2 = float(notaT2Tb.get())
    notaTarea3 = float(notaT3Tb.get())


    
    if asignatura == "Matemáticas":
        definitiva = notaExamen*0.40 + notaTarea1*0.20 + notaTarea2*0.20 + notaTarea3*0.20
        varDefinitiva.set(str(definitiva))

    elif asignatura == "Física":
        definitiva = notaExamen*0.50 + notaTarea1*0.20 + notaTarea2*0.15 + notaTarea3*0.15
        varDefinitiva.set(str(definitiva))

    elif asignatura == "Química":
        definitiva = notaExamen*0.60 + notaTarea1*0.20 + notaTarea2*0.10 + notaTarea3*0.1
        varDefinitiva.set(str(definitiva))

    
    if definitiva > 3:
        varMensaje.set("Aprobo")
    else:
        varMensaje.set("No aprobo")


  
    


#Interfaz gráfica
raiz = Tk()
raiz.title("Definitiva de asignatura")
raiz.resizable(0,0)


#Contenedor componentes de interfaz gráfica
contenedor1 = LabelFrame(raiz, text="Datos", bd = 3)
contenedor1.pack(padx = 5, pady = 5)

nombreALabel = Label(contenedor1, text="Nombre de la Asignatura: ").grid(row=0, column=0, sticky = "w", padx=5, pady=5)
nombreACombo = ttk.Combobox(contenedor1, state="readonly",width=12,values=["Matemáticas", "Física","Química"])
nombreACombo.grid(row=0,column=1,padx=5, pady=5)
nombreACombo.current(0)
notaELabel = Label(contenedor1, text="Nota Examen: ").grid(row=1, column=0, sticky = "w", padx=5, pady=5)
notaETb = Entry(contenedor1, width=10)
notaETb.grid(row=1,column=1, sticky="w", padx=5, pady=5)
notaT1Label = Label(contenedor1, text="Nota Tarea 1: ").grid(row=1, column=2, sticky = "w", padx=5, pady=5)
notaT1Tb = Entry(contenedor1, width=10)
notaT1Tb.grid(row=1,column=3, sticky="w", padx=5, pady=5)
notaT2Label = Label(contenedor1, text="Nota Tarea 2: ").grid(row=2, column=0, sticky = "w", padx=5, pady=5)
notaT2Tb = Entry(contenedor1, width=10)
notaT2Tb.grid(row=2,column=1, sticky="w", padx=5, pady=5)
notaT3Label = Label(contenedor1, text="Nota Tarea 3: ").grid(row=2, column=2, sticky = "w", padx=5, pady=5)
notaT3Tb = Entry(contenedor1, width=10)
notaT3Tb.grid(row=2,column=3, sticky="w", padx=5, pady=5)

definitiaLabel = Label(contenedor1, text="Definitiva: ").grid(row=4, column=0, sticky="w", padx=5, pady=5)
varDefinitiva = StringVar()
definitivaTb = Entry(contenedor1, textvariable=varDefinitiva, state="readonly",width=10)
definitivaTb.grid(row=4, column=1, padx=5, pady=5, sticky="w")
varMensaje = StringVar()
mensajeTb = Entry(contenedor1, textvariable=varMensaje, state="readonly", width=25)
mensajeTb.grid(row=4, column=2,columnspan=2, padx=5, pady=5, sticky="w")


#Contenedor de los botones
contenedor2 = LabelFrame(raiz, text="",bd =3)
contenedor2.pack(padx = 5, pady = 5)

botonIniciar = Button(contenedor2,text="Iniciar",width=10, command=principal).grid(row=0, column=0, padx = 5, pady=5)
botonBorrar = Button(contenedor2,text="Borrar",width=10, command=borrar).grid(row=0, column=1,padx = 5, pady=5)
botonSalir = Button(contenedor2,text="Salir",width=10, command=salir).grid(row=0, column=2,padx = 5, pady=5)

raiz.mainloop()
