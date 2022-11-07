#Se lee el número entero y determine la suma de las cifras

n = int(input("Ingrese un número de cuatro cifras: "))

suma= 0
while n > 0:
    suma = suma + (n % 10)
    n = n // 10
    
print("La suma de los dígitos es: ",suma)


