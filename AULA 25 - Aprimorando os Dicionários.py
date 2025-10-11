galera = []
pessoa = {}

soma = media = 0 

while True : 

    pessoa.clear()
    pessoa['Nome'] = str(input("Nome :"))

    while True : 

        pessoa["Sexo"] = str(input("Sexo [M/F] :")).upper()[0]
        if pessoa["Sexo"] in "MF" :
            break
        print("Erro, somente [M ou F]")

    pessoa["Idade"] = int(input("Idade : "))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())

    while True :
        respota = str(input("Continua [S/N]")).upper()[0]
        if respota in "SN":
            break
        print("Erro, Somente [S / N]")

    if respota == "N":
        break

print("TABELA FINAL")
print(f" A -- O numero de pessoas cadstradas foram {len(galera)}")

media = soma/ len(galera)

print(f" B -- A idade media das pessoas foram {media:5.2f}")

print("A mulheres cadastras foram ", end=" ")
for i in galera :
    if i["Idade"] >= media :
        print(f" ",end=" ")

        for key,value in i.items():
            print(f"{key} == {value}", end=" ")

    print()

print("FIM DO PROGRAMA")