#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas

x = 1
n = int(input("ingresa el total de personas a medir: "));
suma = 0;

while x <= n:

    altura = int(input("ingresa la altura de la persona: "));
    suma = suma + altura
    x = x +1;

promedio = suma / n;

print("la altura promedio de ",n," personas es: ", promedio);