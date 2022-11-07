"""La Fuerza Aérea va a crear un nuevo escuadrón, para combatir un problema de seguridad. Las directivas de la
institución establecieron los siguientes criterios de selección: Los hombres deben cumplir con una altura mínima
de 1.75 mts y las mujeres con una altura mínima de 1.68 mts. Es requisito que la edad del aspirante esté entre 18
y 25 años, ambos inclusive. Naturalmente, no se conoce con anticipación cuántos aspirantes serán evaluados.
Por tanto, se requiere elaborar el diseño modular y la implementación de una propuesta de solución, tal que le
permita a la institución calcular e imprimir, para cada aspirante, su nombre y un aviso indicando si es
seleccionado o no. Además, también se requiere la altura promedio de los hombres seleccionados y la cantidad
total de aspirantes evaluados."""



def hombres():
    acum=0
    n=int(input("Cuantos aspirantes desea evaluar?"))
    for i in range(n):
        nombre=input("Cual es su nombre?: ")
        altura=int(input("Ingrese su altura en centimetros: "))
        edad=int(input("Ingrese su edad: "))
    
        if altura>=175 and edad in range (18,26):
            acum=acum+1
               
            print("Seleccionado")
        
        

        else:
            print("No paso")

    print(acum)

hombres()

