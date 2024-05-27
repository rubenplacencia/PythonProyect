#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos

num1 = int(input("Ingresa el primer numero: "));
num2 = int(input("Ingresa el segundo numero: "));
num3 = int(input("Ingresa el tercero numero: "));


if num1 > num2:
    if num1 > num3:
        print("el numero 1: ", num1, " es el numero mayor");
else:
    if num2 > num3:
        print("el numero 2: ", num2, " es el numero mayor");
    else:
        print("numero 3: ", num3, "es mayor");