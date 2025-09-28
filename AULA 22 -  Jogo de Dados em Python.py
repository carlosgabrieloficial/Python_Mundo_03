from random import randint
from time import sleep
from operator import itemgetter


jogo_dados = {
    'jogador1' : randint(1,6),
    'jogador2' : randint(1,6),
    'jogador3' : randint(1,6),
    'jogador4' : randint(1,6)}
ranking = list

print("VALORES SORTEADOS")

for key, value in jogo_dados.items():
    print(f"{key} tirou {value} no dado")
    sleep(1)

ranking = sorted(jogo_dados.items(), key=itemgetter(1), reverse=True)

print("-="*30)
print("RANKING")

for item,value in enumerate(ranking):
    print(f"{item+1}, lugar {value[0]} com {value[1]}")
