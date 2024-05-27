#Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:

"""
    Nivel máximo:	Porcentaje>=90%.
	Nivel medio:	Porcentaje>=75% y <90%.
	Nivel regular:	Porcentaje>=50% y <75%.
	Fuera de nivel:	Porcentaje<50%.
"""

pTotal = int(input("Ingresa el total de preguntas realizadas: "));
rCorrectas = int(input("Ingresa el total de respuestas correctas: "));

porcentaje = ( rCorrectas / pTotal) * 100;

print(porcentaje);100;

if porcentaje >= 90:
    print("Nivel maximo");
else:
    if porcentaje >= 75:
        print("Nivel medio ");
    else:
        if porcentaje >= 50:
            print("Nivel regular");
        else:
            print("Fuera de nivel");