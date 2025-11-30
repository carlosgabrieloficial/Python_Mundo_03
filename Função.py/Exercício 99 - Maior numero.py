# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#======================================================================================


def maior(*numeros):
    contador = maiorNumero = 0
    for numero in numeros :
        print(f"{numero}", end =" ")
        if contador == 0 :
            maiorNumero = numero
        else:
            if numero > maiorNumero:
                maiorNumero = numero
        contador += 1 

    print(f"Foi informado os numero \n{contador}\n valores ao todo")
    print(f"O maior numero foi {maiorNumero}")
    print()

    
maior(30,23,54,2)
maior(30,23)
maior(2)