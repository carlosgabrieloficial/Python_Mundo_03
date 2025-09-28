## Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols_partida = []


jogador["Nome"] = str(input("Nome :"))
jogador["Numero de Partidas"] = int(input("Qual o numero de partidas jogadas"))

for i in range (jogador["Numero de Partidas"]):
    print(f"Quantos gols na partidas {i}")
    gols = int(input("Quantos gols na partida : ")) 
    jogador["N_gols"].append(gols)

print("=-"*30)
print(jogador)
print("=-"*30)
