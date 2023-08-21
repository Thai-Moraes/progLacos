'''
 Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100)
'''

cont = 0
x = 1

while (x <= 100):
    cont += x
    x += 1

print(f"A soma dos cem primeiros números inteiros é {cont}")