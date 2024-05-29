""" 
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12
"""

base = 0;
altura = 0;
super = 0;
triBase = 0;
n = int(input("ingresa el numero de triangulos: "));

for x in range(n) :
    base = int(input(f"ingresa la base del triangulo {x+1}: "));
    altura = int(input(f"ingresa la altura del triangulo {x+1}: "));
    super = (base * altura) / 2; 
    print(f"la altura de tu triangulo {x} es: {base} y la base {altura} y su base es {super}");
    if super >= 12:
        triBase = triBase + 1;

print(f"triangulos con base mayor a 12: {triBase}");