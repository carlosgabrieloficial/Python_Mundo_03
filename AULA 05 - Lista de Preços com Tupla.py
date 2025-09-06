# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produto_valores = ("lapis","1.75","Borracha","2.00","Carderno","15.90","Estojo","25.00","Trnsferidor","4.20","Compaso","9.90","Mochila","120.00","Canete","22.00","livro","34.90")

print("=="*20)
print("LISTA DE PREÇOS")
print("=="*20)

for posicao in range (0, len(produto_valores)):
    if posicao % 2 == 0 :
        print(f"{produto_valores[posicao]:.<30}", end=" ")
    else:
        print(f"R${produto_valores[posicao]:>7}")

print("=="*20)