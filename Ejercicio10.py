#Imprimir el número al revés

numero = int(input("Ingrese un numero natural de 4 cifras:"))

c4 = numero % 10
c3 = int((numero%100)/10)
c2 = int((numero%1000)/100)
c1 = int((numero - (numero%1000))/1000)

print(f"{c4}{c3}{c2}{c1}")

    