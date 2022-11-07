print("\n========== Bienvenido a una actualización del censo nacional, a continuación ingrese los datos que se le solicitan ==========\n")

nombre=input("Digite su nombre: ")
apellidos=input("Digite sus apellidos: ")
tipodoc=input("Digite su tipo de documento de identidad-de la forma RC,TI,CC,CE-: ")
numdoc=int(input("Digite su número de documento de identidad-sin puntos ni comas-: "))
fecha=input("Digite su fecha de nacimiento-de la forma 00 MES 0000-: ")
departamento=input("Digite su departamento de nacimiento: ")
ciudad=input("Digite su ciudad de nacimiento: ")
direccion=input("Digite su dirección de residencia: ")

CantFamiliares=int(input("Digite la cantidad de familiares a registrar: "))
familiar=""
cont=1
while (CantFamiliares!=0):
    CantFamiliares = CantFamiliares - cont
    familiar= familiar + "\nNombre: " + input("\nDigite el nombre del familiar: ") 
    familiar= familiar + "\n"
    familiar= familiar + "Apellido: " + input("Digite el apellido del familiar: ")
    familiar= familiar + "\n"
    familiar= familiar + "Tido de documento: " + input("Digite el tipo de documento de identidad del familiar-de la forma RC,TI,CC,CE-: ")
    familiar= familiar + "\n"
    familiar= familiar + "NUMERO DE DOCUMENTO: " + str(input("Digite el número de documento de identidad del familiar-sin puntos ni comas-: "))
    familiar= familiar + "\n"
    familiar= familiar + "FECHA DE NACIMIENTO: " + input("Digite la fecha de nacimiento del familiar-de la forma 00 MES 0000-: ")
    familiar= familiar + "\n"
    familiar= familiar + "PARENTEZCO: " + input("Digite el parentesco que tiene el familiar con usted: ")
    familiar= familiar + "\n"
        
print("\n===== JEFE/A DEL HOGAR =====\n" "\nNOMBRE: ", nombre, "\n" "APELLIDOS: ", apellidos,"\n" "TIPO DE DOCUMENTO: ", tipodoc, "\n" "DOCUMENTO: ", numdoc, "\n" "FECHA DE NACIMIENTO: ", fecha, "\n" "DEPARTAMENTO: ", departamento, "\n" "CIUDAD: ", ciudad, "\n" "DIRECCIÓN: ", direccion, "\n")
print("\n===== FAMILIARES =====\n" + familiar)
