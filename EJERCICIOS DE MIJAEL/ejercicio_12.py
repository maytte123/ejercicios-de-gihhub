import os
os.system("cls")

'''Dado un número que expresa el tiempo en segundos, desarrolle el programa que exprese dicho tiempo
 como la cantidad de días, horas, minutos y segundos contenidos en ese número.'''
print("")
num_segundos=int(input("digite en numero expresados en segundos:"))
dias=((num_segundos//60)//60)//24
horas=((num_segundos//60)//60)%24
minutos=(num_segundos//60)%60
segundos=num_segundos%60
print("dias",dias)
print("horas",horas)
print("minutos",minutos)
print("segundos",segundos)
print("")
