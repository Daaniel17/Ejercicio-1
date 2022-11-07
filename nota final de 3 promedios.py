def notafinal(c1,c2,c3):
    return c1*0.3+c2*0.35+c3*0.35/3
    
def principal():
    pi1 = float(input("Ingrese la nota de la practica individual del corte 1: "))
    ee1 = float(input("Ingrese la nota de la evaluacion escrita del corte 1: "))
    tc1 = float(input("Ingrese la nota del trabajo en clase del corte 1: "))

    promedio1 = pi1*0.2+ee1*0.6+tc1*0.60/3
    print ("El promedio del corte 1 es: "+str(promedio1))
    
    pi2 = float(input("Ingrese la nota de la practica individual del corte 2: "))
    ee2 = float(input("Ingrese la nota de la evaluacion escrita del corte 2: "))
    tc2 = float(input("Ingrese la nota del trabajo en clase del corte 2: "))

    promedio2 = pi2*0.2+ee2*0.6+tc2*0.60/3
    print ("El promedio del corte 2 es: "+str(promedio2))

    pi3 = float(input("Ingrese la nota de la practica individual del corte 3: "))
    ee3 = float(input("Ingrese la nota de la evaluacion escrita del corte 3: "))
    tc3 = float(input("Ingrese la nota del trabajo en clase del corte 3: "))

    promedio3 = pi3*0.2+ee3*0.6+tc3*0.60/3
    print ("El promedio del corte 3 es: "+str(promedio3))

    definitiva = notafinal(promedio1, promedio2, promedio3)

    print("La nota definitiva o final fue: "+str(definitiva))

    

principal()
