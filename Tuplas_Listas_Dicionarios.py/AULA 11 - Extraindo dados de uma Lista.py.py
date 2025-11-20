#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input("Digite um valor : ")))
    respota = str(input("Quer continuar ? [S/N]"))
    if respota in "Nn":
        break

print("="*30)
print(f"Você digitou {len(lista)}")
lista.sort(reverse=True)
print(f"Os valores em ordem decrecente é {lista}")
if 5 in lista:
    print("tem o valor 5 na lista")
else:
    print("nao tem o valor 5 na lista ")