"""Una fábrica de computadoras planea ofrecer a los clientes un descuento que
dependerá del número de computadoras que compre. Si las computadoras
son menos de 5 se le dará un 10% de descuento sobre el total de la compra,
si el número de computadoras es mayor o igual a 5 pero menos de 10, se le
otorgará un descuento del 20%; y si son 10 o más se les dará un 40% de
descuento.

La factura de venta debe mostrar: Nombre de Cliente, Cantidad de
Computadoras a comprar, precio unitario, precio total, descuento obtenido y
valor total a pagar.
Asuma que el programa deberá registrar los datos para 3 ventas"""


def principal():
    total=float
    descuento=float
    cliente=str(input("Ingrese el nombre de el cliente: "))
    numcomputadores=int(input("ingrese el numero de cumputadoras a comprar: "))
    total = numcomputadores*11000
    unitario= total/numcomputadores

    if numcomputadores < 5:
        descuento= total* .10
    elif numcomputadores >= 5 and numcomputadores < 10:
        descuento= total* .20
    elif numcomputadores >= 10:
        descuento= total* .40
    else:
        print("Digite lo que se le ha solicitado")
    
    all=total-descuento

    print("Señor ",cliente,"Usted ha comprado ", numcomputadores,"computadoras " + "El precio unitario es: ",unitario,"El precio total es: ", total,"el descuento obtenido es: ", descuento, "el valor total a pagar es: ", all)
        
principal()



