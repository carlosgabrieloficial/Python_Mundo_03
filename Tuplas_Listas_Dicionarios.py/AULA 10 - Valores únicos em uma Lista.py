lista = []

while True:
    numero = int(input("Digite um valor :"))
    if numero not in lista:
        lista.append(numero)
        print("O valor foi adicionado")
    else:
        print("Numero ja digitado, Tente novamente")

    resposta = str(input("Quer continuar [S/N] :"))
    if resposta in "Nn":
        break
lista.sort()

print(lista)

    
