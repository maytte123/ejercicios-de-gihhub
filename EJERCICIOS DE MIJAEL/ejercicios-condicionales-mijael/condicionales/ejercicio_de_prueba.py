import os
os.system("cls")
'''14.	En un supermercado hay una promoción según la cual el cliente raspa una tarjeta que contiene
 un número oculto. Si el número de la tarjeta es par no menor de 100, el cliente obtiene un descuento 
 del 15 %,caso contrario será del 5 % sobre el importe de la compra.  Desarrolle el programa que 
 muestre el número de la tarjeta, el monto de la compra y el descuento.'''
print("")
total=1000
print('''¡¡¡Bienvenido al banco!!!\n
    que quieres hacer\n\
    1.- ingresar dinero\n\
    2.- sacar dinero\n\
    3.- salir\n''')
opcion=int(input())
if opcion==1:
    ingreso=float(input("¿cuanto dinero deseas ingresar?"))
    total+=ingreso
    print(f"tu saldo es de{total:1f}")
if opcion==2:
    egresos=float(input("¿cuanto dinero deseas sacar?:"))
    total-=egreso
    print(f"tu saldo es de{total:2f}")
if opcion==3:
    quit()
    






