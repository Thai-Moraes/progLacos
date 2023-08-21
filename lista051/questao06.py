'''
 Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da
multiplicação sucessiva de n por 3 enquanto o produto for menor que 250. (n x 3; n x 3 x 3; n x 3 x 3 x 3 etc...).
'''

n = int(input("Coloque um número: "))

while n > 50:
    n = int(input("Coloque um OUTRO número: "))

i = 0
produto = i * 3

while i <= n and produto < 250:
    produto = i * 3
    i += 1
    print(produto)

print(f"\nO produto de n vezes de três é igual a {produto}")