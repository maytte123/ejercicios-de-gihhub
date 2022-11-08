



primer_numero=input("Escribir el primer numero:")
segundo_numero=input("Escribir el segundo  numero:")
tercer_numero=input("Escribir el tercer numero:")

if primer_numero>segundo_numero:
   medio =primer_numero
   xtem = segundo_numero
else:
   medio = segundo_numero
   xtem = primer_numero
if medio > tercer_numero :
   medio = tercer_numero
if medio < xtem :
   medio = xtem
print("El número Medio es : ",medio)
