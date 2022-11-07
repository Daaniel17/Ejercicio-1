'''Crea un programa, en el que el usuario
introduzca una frase y el programa calcule en número de palabras de
dicha frase.'''

frase=input("Introduzca la frase: ")

contar=len(frase.split())
print(contar)
