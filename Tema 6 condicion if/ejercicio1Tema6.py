#Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

num1 = int(input("Ingresa el primer numero: "));
num2 = int(input("ingresa el segundo numero:"));

if num1 > num2:
    suma = num1 + num2;
    diferencia = num1 - num2;
    print("la suma es: ", suma, "y la diferencia es: ", diferencia);
else:
    if num2 > num1:
        producto = num1 * num2;
        division = num1 / num2;
        print("el producto es: ", producto, "y la division es: ", division)
    else:
        print("los numeros son iguales");