"""
Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
"""

num1 = int(input("Ingresa un numero entero: "));

if num1 <= 9:
    print("el numero tiene solo 1 digito");
else:
    print("el numero tiene 2 digitos");