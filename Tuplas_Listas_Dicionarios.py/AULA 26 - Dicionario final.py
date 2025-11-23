time = []
jogador = {}

while True:
    jogador = {}  # Crie um novo dicionário a cada iteração
    jogador["Nome"] = str(input("Nome: "))
    n_partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou na carreira: "))
    partida = []  # Crie uma nova lista para as partidas

    for i in range(n_partidas):
        partida.append(int(input(f"Diga quantos gols fez na partida {i+1}: ")))
    jogador["Gols"] = partida[:]
    jogador["Soma"] = sum(partida)
    time.append(jogador.copy())  # Adicione o dicionário "jogador" à lista "time"

    while True:
        continuar = str(input("Deseja continuar [S/N]? ")).upper()[0]
        if continuar in "SN":
            break
        print("Erro! Tente novamente, responda com [S ou N].")

    if continuar == "N":
        break

# Exibir cabeçalho
print("CÓDIGO")
for i in jogador.keys():
    print(f"{i:<15}", end=" ")
print()

# Exibir as informações dos jogadores
for key, v in enumerate(time):
    print(f"{key:>3}", end=" ")
    for i in v.values():
        print(f"{str(i):<15}", end=" ")
    print()

print("-=" * 40)

# Exibir dados de jogadores individuais
while True:
    busca = int(input("Mostrar dados de qual Jogador (999 para sair): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! Não existe jogador com esse código {busca}.")
    else:
        print(f"--- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']} ---")
        for i, g in enumerate(time[busca]["Gols"]):
            print(f"No jogo {i+1} fez {g} gols.")

print("--- VOLTE SEMPRE ---")
