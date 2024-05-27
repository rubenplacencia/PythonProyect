#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
x = 1;
mayor = 0;
menor = 0;
while x <= 10:
    nota = int(input("ingresa la nota del alumno: "));

    if nota >= 7:
        mayor = mayor + 1;
    else:
        menor = menor + 1;

    x = x + 1;

print("alumnos que pasaron: " ,mayor, "alumnos que no pasaron: " ,menor)