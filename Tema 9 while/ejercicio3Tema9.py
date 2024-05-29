#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

n = int(input("ingresa el numero de trabajadores: "));
x = 1;
importe = 0;
menor = 0;
mayor = 0;

while x <= n:
    sueldo = int(input("Ingresa el sueldo del trabajador: "));

    if sueldo >= 100 and sueldo <= 300:
        menor = menor + 1;
    else:
        if sueldo >= 300:
            mayor = mayor + 1;
    x = x + 1;
    importe = importe + sueldo;

print("la empresa gasta en sueldos: ", importe, "empleados que cobran entre 100 y 300 : ", menor, "empleados que ganan mas de 300: ", mayor);

