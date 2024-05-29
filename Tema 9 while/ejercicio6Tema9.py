""" 
Realizar un programa que permita cargar dos listas de 3 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""
y = 1;
x = 1;
suma1 = 0;
suma2 = 0;

while x <= 3:
    if y <= 3:
        while y <= 3:
            lista1 = int(input("ingresa el valor de la list 1: "));
            suma1 = suma1 + lista1;
            y = y + 1;
    else:
        lista2 = int(input("Ingresa el valor  de la lista 2: "));
        suma2 = suma2 + lista2;
        x = x + 1;

if suma1 > suma2:
    print("lista 1 es mayor");
else:
    print("la lista 2 es mayor");
 