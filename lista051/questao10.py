"""
 Desenvolver um programa que apresente as potências de 3 variando de 0 a 15. Deve ser considerado que
qualquer número elevado a zero é 1, e elevado a 1 é ele próprio. A apresentação deve observar a seguinte
exibição na tela:
3 elevado à 0 = 1
3 elevado à 1 = 3
3 elevado à 2 = 9
(...)
3 elevado à 15 = 14348907
"""
import math

# Math.pow

cont = 0

while (cont <= 15):
    print(f"3 elevado à {cont} = {math.pow(3, cont):.0f}")
    cont += 1

# SEM Math.pow
print("\n\n")
cont = 0

while (cont <= 15):
    pow = 3 ** cont

    print(f"3 elevado à {cont} = {pow:.0f}")
    cont += 1
