'''
 Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da
multiplicação sucessiva de n por 3 enquanto o produto for menor que 250. (n x 3; n x 3 x 3; n x 3 x 3 x 3 etc...).
'''

n = int(input("Coloque um número menor ou igual a 50: "))

while n > 50:
    n = int(input("Coloque um número MENOR OU IGUAL A 50: "))


while n < 250:
    print(n)
    n = n * 3