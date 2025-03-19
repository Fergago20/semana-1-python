def evaluacion (num):
    if num < 100:
        return "Menor que 100"
    else :
        return "Mayor a 100"
   

valor =input("Introduce un número: \n")
print(evaluacion(int(valor)))