import os
os.system("cls")

pies = float (input("Escriba la cantidad en pies:" ))
pulgadas = float (input("Escriba la cantidad en pulgadas:" ))
tpies=pies*30.48
tpulgadas=pulgadas*2.54
total_en_cm=tpies+tpulgadas
total_en_m=total_en_cm/100
print("total de tallas en metros",total_en_m,"m" ) 

