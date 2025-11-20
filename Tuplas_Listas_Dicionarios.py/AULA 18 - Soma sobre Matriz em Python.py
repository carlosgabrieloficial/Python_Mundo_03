
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = soma_coluna = maior_valor = 0
for linha in range(0,3):

    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um numero, na posição[{linha},{coluna}]"))

print("=="*20)
for linha in range (0,3):
    for coluna in range (0,3):
        print(f"{matriz[linha][coluna]:^5}", end=" ")
        if matriz[linha][coluna] % 2 == 0 :
            soma_par += matriz[linha][coluna]


    print()

print(f"a soma dos numeros pares foram {soma_par}")

for linha in range (0,3):
    soma_coluna += matriz[linha][2]

print(f"A soma da terceira coluna é {soma_coluna}")

for coluna in range (0,3):
    if coluna == 0 :
        maior_valor = matriz[1][coluna]
    elif matriz[1][coluna]>maior_valor:
        maior_valor = matriz[1][coluna]

print (f"O maior numero é {maior_valor}")
