#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.

num1 = int(input("Ingresa un numero: "));

if num1 <= 9:
    print("el numero tiene 1 cifra");
else:
    if num1 <= 99:
        print("el nmero tiene 2 cifras");
    else:
        if num1 <= 999:
            print("el numero tiene 3 cifras");
        else:
            print("el numero tiene mas de 3 cifras");