#área y volumen de un cilindro#

import math

radio=float(input("Ingresa radio del cilindro "))
altura=float(input("Ingresa la altura del cilindro "))

area=2*math.pi*radio*(radio+altura)
volumen=(math.pi*(radio)**2)*altura

print(f"El area del cilindro es: {area} cm²")
print(f"El volumen del cilindro es: {volumen} cm³")
