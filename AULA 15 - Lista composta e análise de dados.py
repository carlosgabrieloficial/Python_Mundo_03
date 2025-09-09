#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
maiores_pesos =  []
menores_pesos = []

while True:
    temp.append(str(input("NOME :")))
    temp.append(float(input("PESO :")))

    if len(princ) == 0 :     #aqui o menor e maior são os mesmo numero
        maiores_pesos = menores_pesos = temp[1]

    else:
        if temp[1] > maiores_pesos:
            maiores_pesos = temp[1]
        if temp[1] < menores_pesos:
            menores_pesos = temp[1]
    princ.append(temp[:])
    temp.clear()

    respota = str(input("Quer continuar [S/N] :"))
    if respota in "Nn":
        break

print("=="*20)

print(f"Você cadastrou esse numero de pessoas {len(princ)}\n", end="")

print(f"O maior peso foi de {maiores_pesos} Kg", end=", ")

for pessoa in princ:
    if pessoa[1] == maiores_pesos:
        print(f"{pessoa[0]}", end=" ")

print(f"\nO menor peso foi de {menores_pesos} Kg", end=", ")

for pessoa in princ:
    if pessoa[1] == menores_pesos:
        print(f"{pessoa[0]}", end=" ")