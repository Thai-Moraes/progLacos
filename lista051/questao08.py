"""
Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo.
"""

cont = 0

print("Os números ímpares na faixa de 0 a 20 são...:\n")

while (cont <= 20):
    if cont % 2 == 1:
        print(cont)
    cont += 1