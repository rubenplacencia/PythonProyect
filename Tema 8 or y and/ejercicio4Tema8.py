""" 
Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
"""

x = int(input("Ingresa la primera cordenada: "));
y = int(input("Ingresa la segunda cordenada: "));


if x > 0 and y > 0:
    print("Esta en el primer cuadrante");
else:
    if x < 0 and y > 0:
        print("Esta en el segundo cuadrante");
    else:
        if x < 0 and y < 0:
            print("esta en el tercero");
        else:
            if x > 0 and y < 0:
                print("esta en el cuarto cuadrante");