"""
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be. (Sem usar Math.pow();)
"""
base = int(input("Informe uma base: "))
exp = int(input("Informe um expoente: "))

cont = 1
potencia = base

print(f"O resultado da potência é {base ** exp}")

while (cont < exp):
    potencia = potencia * base
    cont += 1

print(f"O resultado da potência é {potencia}")
