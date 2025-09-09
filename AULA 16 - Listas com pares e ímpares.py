##Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


lista_todo_num = [[],[]]
numero = 0

for i in range (0,7):
    numero = int(input("digite um numero :"))

    if numero % 2 == 0 : # aqui se o numero é par
        lista_todo_num[0].append(numero)

    else:                # aqui se o numero é par
        lista_todo_num[1].append(numero)

print(lista_todo_num)
lista_todo_num[0].sort
lista_todo_num[1].sort
print(lista_todo_num[0])
print(lista_todo_num[1])