from random import randint

def sorteio(listaNum):

    print("SORTEANDO 5 VALORES A LISTA", end=" ")
    for i in range (0,5):
        num = randint(1, 10)
        listaNum.append(num)
        print(f"{num}", end=" ")
    print("PRONTO")


def somaPar(listaNum):

    soma = 0 
    for valor in listaNum:
        if valor % 2 == 0:
            soma+= valor
    print(f"SOMA DOS VALORES PARES DA LISTA {listaNum}, soma {soma}")


n = list()
sorteio(n)
somaPar(n)
