"""
 Desenvolver um programa que imprima a tabuada de 3 a 6
"""

tabuada = 3
cont = 1


while cont <= 10 and tabuada <= 6:
    print(f"{tabuada} . {cont} = {tabuada * cont}")
    cont += 1

    if cont == 11:
        print("\n")
        tabuada += 1
        cont = 1

