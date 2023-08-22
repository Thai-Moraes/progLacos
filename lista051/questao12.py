"""
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da media entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da media
"""
import math

num = int(input("Informe um número (-1 para realizar a operação): "))

maior = num
menor = num
media = num
i = 1

while num != -1:
    num = int(input("Informe um número (-1 para realizar a operação): "))

    if num != -1:
        media += num
        i += 1

        if maior < num:
            maior = num

        elif menor > num:
            menor = num

print(f"\nO maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"A media é igual a: {float(media / i)} ")