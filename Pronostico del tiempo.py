def principal():
    temp= int(input("ingrese temperatura: "))
    vient=int(input("ingrese el viento: "))
    humed=float(input("ingrese la humedad: "))
    if temp > 25 and vient < 10 and humed < 33:
        print("El pronostico es soleado")
    elif 20 <= temp <= 30 and vient < 10 and humed > 90:
        print("El pronostico es Humedo")
    elif 0 <= temp <= 10 and vient > 5 and 80 >= humed >= 40:
        print("El pronostico es frio")
    elif -5 <= temp < 0 and vient < 5 and humed > 50:
        print("El pronostico es nieve") 
    else:
        print("No cumple los parametros")
        principal()   
principal()
