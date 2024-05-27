#Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.

num1 = int(input("Ingresa el primer numero: "));
num2 = int(input("Ingresa el segundo numero: "));
num3 = int(input("Ingresa el tercero numero: "));
num4 = int(input("Ingresa el cuarto numero: "));

suma = num1 + num2 + num3 + num4;
promedio = suma / 4;

print("la suma de los 4 numeros es: ", suma, "y el promedio es: ", promedio);