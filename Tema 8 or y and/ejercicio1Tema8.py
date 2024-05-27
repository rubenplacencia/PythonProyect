#Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.

dia = int(input("ingresa el dia: "));
mes = int(input("ingresa el mes: "));


if dia == 25 and mes == 12:
    print("Feliz navidad !!!!");
else:
    print("no es navidad :c ");