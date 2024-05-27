""" 
Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)
"""

num1 = int(input("ingresa el primer numero: "));
num2 = int(input("ingresa el segundo numero: "));
num3 = int(input("ingresa el tercero numero: "));


if num1 > num2 and num1 > num3:
    vMaximo = num1;
else:
    if num2 > num3 and num2 > num1:
        vMaximo = num2;
    else: 
        vMaximo = num3;

if num1 < num2 and num1 < num3:
    vMinimo = num1;
else:
    if num2 < num3 and num2 < num1:
        vMinimo = num2;
    else: 
        vMinimo = num3;

rVariacion = vMaximo - vMinimo;

print("El rango de variacion es: ", rVariacion, "Mayor: ", vMaximo, "Menor: ", vMinimo);

