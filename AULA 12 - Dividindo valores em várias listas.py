#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

lista = [], lista_num_par = [], lista_num_impar = []

while True:
    num = (int(input("Digite um numero : ")))
    lista.append(num)

    if num % 2 == 0 :
        lista_num_par.append(num)

    else:
        lista_num_impar.append(num)

    resposta = str(input("Deseja continuar [S/N] : "))
    if resposta in "Nn":
        print("FIM")
        print("=="*20)
        print(f"Essa foi a sua lista inteira\n {lista}")
        print(f"Esse são os numeros pares {lista_num_par}")
        print(f"Esses são os numeros impares {lista_num_impar}")
        break