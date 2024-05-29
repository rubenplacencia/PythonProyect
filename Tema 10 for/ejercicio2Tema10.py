#Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados

numero =0;
suma = 0;

for x in range(1,11):
    numero = int(input("ingresa un numero: "));
    print(x);
    if x >= 6 and x <= 10:
        suma = suma + numero;

print(f"la suma de los ultimos 5 digitos es: {suma}");