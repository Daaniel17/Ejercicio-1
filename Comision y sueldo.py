"""Un vendedor recibe un sueldo base de $420.000 más un 10% extra por
comisión de cada una de sus ventas durante el mes, tenga en cuenta que se
realizan descuentos sobre el sueldo base así: aporte a salud 4% y pensiones
4%. El vendedor desea saber cuál será el total de la comisión si hizo 3 ventas
al mes, y cuánto será el total del dinero que recibirá en su sueldo."""


sueldo=420000
salud=0.04
pension=0.04
descuento=sueldo*(salud+pension)
extra=0.10

venta_1=int(input("Ingrese el valor de la venta 1: "))
venta_2=int(input("Ingrese el valor de la venta 2: "))
venta_3=int(input("Ingrese el valor de la venta 3: "))

comision=(venta_1 + venta_2 + venta_3)* extra
pago=comision
sueldoTotal=sueldo-descuento



print("El total de su comision es: ", pago)
print("El total de su sueldo es: ", sueldoTotal)
