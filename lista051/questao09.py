"""
Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2.
"""

cont = 0
x = 0

while (x <= 500):
    if x % 2 == 0:
        cont += x
    x += 1

print(f"A soma dos valores pares de 0 até 500 é {cont}")