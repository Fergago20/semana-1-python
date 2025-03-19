"""
ultimo problema"""

import os

def pago (horas, salario):
    if horas <= 48:
        return horas * salario
    else:
        return 48 * salario + (horas - 48) * salario * 2
    
horas = int(input("Ingrese el número de horas trabajadas: \n"))
salario = float(input("Ingrese el salario por hora: \n"))
print("El pago total es: ", pago(horas, salario))
os.system("pause")
os.system("cls")