def imc(p,e):
    return (p/e**2)

def principal():
    Peso= float(input("Ingrese su peso en kilos: "))
    Estatura= float(input("Ingrese su estatura en metros: "))

    IMC= imc(Peso,Estatura)
    
    print ("El imc obtenido es: "+str(IMC))

    if float(IMC) < 18.5:
        print ("su estado de imc es: bajo peso")
    elif 18.5 < float(IMC) < 24.9:
        print ("su estado de imc es: peso normal")
    elif 25 < float(IMC) < 29.9:
        print ("su estado de imc es: sobrepeso")
    elif float(IMC) >= 30:
        print ("su estado de imc es: Obesidad Tipo 1")

    return principal
principal()

