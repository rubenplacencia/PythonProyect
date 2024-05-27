#Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda "Todos los números son menores a diez".

num1 = int(input("Ingresa el primer numero: "));
num2 = int(input("Ingresa el segundo numero: "));
num3 = int(input("Ingresa el tercer numero: "));

if num1 < 10 and num2 < 10 and num3 < 10:
    print("todos los numeros son menores a 10");
else:
    print("hay un valor mayor a 10");