#Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"


nota1 = int(input("Ingresa la primera nota: "));
nota2 = int(input("Ingresa la segunda nota: "));
nota3 = int(input("Ingresa la tercera nota: "));

suma = nota1 + nota2 + nota3;
promedio = suma / 3;

if promedio >= 7:
    print("pasaste la materia!!");
else:
    print("Reprobaste la materia!!");