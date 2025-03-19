import os
def clasificar (nota):
    if nota < 60:
        return 'Reprobado'
    elif nota >=60 and nota < 70:
        return 'Regular' 
    elif nota >= 70 and nota < 80:
        return 'Bueno'
    elif nota >= 80 and nota < 90:
        return 'Muy bueno'
    elif nota >= 90 and nota <= 100:
        return 'Excelente'
    else:
        return 'Nota no válida'
    
numestudiantes = int(input("Ingrese el número de estudiantes: \n"))
for i in range(numestudiantes):

    nota = int(input("Ingrese la nota del estudiante: \n"))
    print(clasificar(nota))
    os.system("pause")
    os.system("cls")
