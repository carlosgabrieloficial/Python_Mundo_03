## Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []


jogador["Nome"] = str(input("Nome :"))

Numero_Partidas = int(input("Qual o numero de partidas jogadas"))
for i in range (Numero_Partidas):

    gols.append(int(input(f"Quantos gols na partida {i+1} : ")))

    jogador["Gols"] = gols[:]

    jogador["Total de Gols"] = sum(gols)

print("=-"*30)
print(jogador)
print("=-"*30)

for key,value in jogador.items():
    print(f"O campo {key} tem valor {value}")

print("=-"*30)

print(f"O jogador {jogador["Nome"]}, jogou {Numero_Partidas} jogos")
 
for i,value in enumerate(jogador["Gols"]):
    print(f" ---> Na partida {i},fez {value} gols")

print(f"O total de jogos é {jogador["Total de Gols"]}")
