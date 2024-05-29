""" 
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
"""
x = 1;
numero = 0;
par = 0;
impar =0;

n = int(input("Ingresa la cantidad de numeros: "));


while x <= n:

    numero = int(input("Ingresa un numero entero: "));

    if numero % 2 == 0:
        par = par + 1;
    else:
        impar = impar + 1;
    x = x+1;

print("hay ", par, " numeros pares y ", impar, " impares");