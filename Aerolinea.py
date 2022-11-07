def lejosDeTierra():

    cantidadM=int(input(" \nIngrese la cantidad de pasajeros: "))
    suma=0
    precioxcant=40
    
    for i in range(cantidadM):
        
        maletas=int(input(" \nCuantas maletas lleva este pasajero?: "))
        suma=suma+maletas
        total=(precioxcant*maletas)
        print("Este pasajero pago un total de ",total,"Dolares.")
       

    print(" \nCantidad maletas transportadas por la empresa fue: ",suma)
    
    print(" \nLa cantidad de pasajeros que no pagaron cuota de mantenimiento es: 0")

    print()
    

def cieloAbierto():

    cantidadM=int(input(" \nIngrese la cantidad de pasajeros: "))
    
    precioxcant=50
    preciok=10
    minimo=23.0
    aumento=0.1
    cantTotal=0
    
    for i in range(cantidadM):
        
        maletas=int(input("Cuantas maletas lleva este pasajero?: "))
        pesoM=int(input("Ingrese el peso de la maleta en kilogramos: "))
        
        
        if maletas==1 and pesoM<=23:
            paga=0
            print("\nEste pasajero pagó: ",paga)
            cantTotal=cantTotal+1
                  
        elif maletas==1 and pesoM>23:
            pagan=(pesoM-23)*10            
            
            total=(pagan)               
            print("\nEste pasajero pago: ",total," Dolares")
            print("\nLa cantidad de pasajeros que no pagaron cuota de mantenimiento es:0 ")

        elif maletas>1:
            total2=(precioxcant*maletas)

            print("\nEste pasajero pagó: ", total2)

        else:
            print("Error")
            
    print("\nLa cantidad de pasajeros que no pagaron cuota fue: ",cantTotal)
    
  
        
while True:
    print("\n****Menu****")
    
    print("Que empresa desea consultar?: ")
    print("1. Lejos de tierra")
    print("2. Cielo")

    opc=input("Ingrese una opcion: ")

    if opc=="1":
        lejosDeTierra()

    elif opc=="2":
        cieloAbierto()

    else:
        print("\nOpcion incorrecta.")

  

    
        
        
