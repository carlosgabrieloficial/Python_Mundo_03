from random import randint
from time import sleep

lista = list()
jogos = list()

print("="*20)
print("MEGA SENA")
print("="*20)

quantidade_jogos = int(input("Quantos jogos gostaria ? "))
total = 1 

while total <= quantidade_jogos:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador +=1 
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1 

print(f"SORTEADOS {quantidade_jogos} JOGOS")
for i ,l in enumerate(jogos):
    print(f"JOGO {i+1}, {l}")
    sleep(1)

print("\nBoa sorte")






