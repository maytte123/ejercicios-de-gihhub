import os
os.system("cls")

mujeres = float (input("Escribir el numero de mujeres:" ))
hombres= float (input("Escribir el total de hombres:" ))

total=mujeres+hombres
print("El porcentaje de mujeres es:",(mujeres/total)*100,"%")
print("El porcentaje de hombres es:",(hombres/total)*100,"%")
