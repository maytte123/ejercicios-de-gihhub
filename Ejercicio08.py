#Área base, área lateral y área total

import math

radio=float(input("Ingresa el radio del un cilindro: "))
altura=float(input("Ingresa la altura del cilindro: "))

area_base=math.pi*(radio)**2 
area_lateral=2*math.pi*radio*altura
area_total=(2*(math.pi*(radio)**2))*(2*math.pi*radio*altura)

print(f"El area base del cilindro es: {area_base} cm³")
print(f"El area lateral del cilindro es: {area_lateral} cm²")
print(f"El area lateral del cilindro es: {area_total} cm²")