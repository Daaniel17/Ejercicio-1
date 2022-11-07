def area_terreno(A,B,C):
    return ((B*(A-C))/2)+(B*C)
def principal():
    magnitud_1 = float(input("Ingrese Magnitud 'A': "))
    magnitud_2 = float(input("Ingrese Magnitud 'B': "))
    magnitud_3 = float(input("Ingrese Magnitud 'C': "))

    area = area_terreno(magnitud_1, magnitud_2, magnitud_3)

    print("El área del terreno es: " + str(area))
    
principal()
