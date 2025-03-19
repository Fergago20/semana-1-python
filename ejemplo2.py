def numeropar(num):
    if num % 2 == 0:
        return "Es par"
    else:
        return "Es impar"
    
valor = input("Introduce un número: \n")
print(numeropar(int(valor)))