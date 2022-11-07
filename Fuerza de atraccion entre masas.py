import math

def principal():
    M1=float(input("Ingrese la masa uno: "))
    M2=float(input("Ingrese la masa dos: "))
    R=float(input("Ingrese la distancia: "))
    G=float(0.00000006673)
    f=G*M1*M2/(R*R)
    print("la fuerza de atraccion entre las masas es: ",f)

principal()

