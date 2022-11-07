'''1. Crea un programa, que dados dos vectores
ordenados realice la fusión de ambos para obtener un tercer vector
también ordenado. Cada vector contiene cinco elementos. '''

import numpy as np

vector_uno = np.array([1,3,5,7,9])
vector_dos= np.array([2,4,6,8,10])

vector_tres=np.union1d(vector_uno,vector_dos)
print(vector_tres)


