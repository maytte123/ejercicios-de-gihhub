#Ejercicio 5 de condicionales

numero = input("Ingrese el numero de 4 cifras: ")

if len(numero) !=4:
    print("El numero debe ser de 4 cifras")

else:
    cifra_men = 10;
    cifra_may = 0;

    for cifra in numero:
        if (int(cifra) < cifra_men):
            cifra_men = int(cifra);

        elif (int(cifra) > cifra_may):
            cifra_may = int(cifra);
    
    print(f"El mayor número posible es: {str(cifra_may)}{str(cifra_men)}");
    
        