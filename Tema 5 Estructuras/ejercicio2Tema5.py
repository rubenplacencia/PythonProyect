#Escribir un programa en el cual se ingresen cuatro números, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto


num1 = 0;
num2 = 0;
num3 = 0;
num4 = 0;

print("ingresa 4 numeros");

num1 = int(input("inregsa el primer numero: "));
num2 = int(input("inregsa el segundo numero: "));
num3 = int(input("inregsa el tercer numero: "));
num4 = int(input("inregsa el cuarto numero: "));

suma = num1 + num2; 

producto = num3 * num4;

print("la suma de", num1, "y", num2, "es: ", suma);
print("El producto de ", num3, "y", num4, "es: ", producto);


