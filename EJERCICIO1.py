#Calcula la longitud de 3 circunferencias y el area total

import math

R1=int(input("ingrese el radio de la primera circunferencia: "))
R2=int(input("ingrese el radio de la segunda circunferencia: "))
R3=int(input("ingrese el radio de la tercera circunferencia: "))

def calculo(R):
   return R * 2 * math.pi

def area(R):
    return math.pi*R**2

l1=calculo(R1)
l2=calculo(R2)
l3=calculo(R3)
A1=area(R1)
A2=area(R2)
A3=area(R3)

total1=l1+l2+l3
total2=A1+A2+A3

print("la longitud de las tres circunferencias es: ",total1, "y el area total es: ",total2)


