#Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora

horas = int(input("Ingresa las horas trabajadas: "));
valorH = int(input("Ingresa el precio por hora: "));

totatlHoras = horas * 30;
salario = totatlHoras * valorH;

print("El trabajador recibe: ", salario, "por mes");109