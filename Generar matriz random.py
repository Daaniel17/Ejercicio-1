from random import randint
import numpy as np
import random

def generarMatriz(n):
    matriz = []

    for i in range(n):
        fila = []
        
    
        for j in range(n):
            fila.append(randint(3,7))

        matriz.append(fila)

    return matriz


resultado = generarMatriz(5)
print(resultado)































