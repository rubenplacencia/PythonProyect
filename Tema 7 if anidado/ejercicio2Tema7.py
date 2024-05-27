#Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

num1 = int(input("Ingresa un numero entero: "));

if num1 > 0:
    print("El numero es positivo !!");
else:
    if num1 < 0:
        print("el numero es negativo");
    else: 
        print("el numero es cero");
