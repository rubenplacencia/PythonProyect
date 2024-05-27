#Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero.

num1 = int(input("ingresa el primer numero: "));
num2 = int(input("ingresa el segundo numero: "));
num3 = int(input("ingresa el tercer numero: "));

if num1 == num2 and num1 == num3 and num2 == num3:
    suma = num1 + num2;
    mult = suma * num3;
    print("la suma de los 2 primeros numeros es: ", suma, "y le multiplicacion: ", mult);
else:
    print("algun numero es diferente ");10

