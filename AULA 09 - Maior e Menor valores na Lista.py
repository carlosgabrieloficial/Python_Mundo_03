valor = []

for contador in range (0,6):
    numero = int(input("Digite um valor"))
    if contador == 0 or numero > valor[-1]: ##aqui voce estar conferindo o ultimo numero
        valor.append(numero)                ##se o numero nao repetir voce adiciona

        print("Adicionado ao final da lista ...")

    else:
        posicao = 0
        while posicao < len(valor):
            if numero <= valor[posicao]:
                valor.insert(posicao,numero)
                print(f"Adicionado na posição {posicao} na lista...")
                break
            posicao += 1

print("="*20) 
print(f"Os valores digitados em ordem do foram {valor}")
