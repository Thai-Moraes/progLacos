"""
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
"""
import math

num = int(input("Informe um número: "))

maior = num
menor = num

while num != -1:
    num = int(input("Informe um número: "))

    if maior < num:
        if num != -1:
            maior = num

    elif menor > num:
        if num != -1:
            menor = num

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")