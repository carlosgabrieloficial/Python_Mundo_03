#grupo = [["Gustavo",19],["Ana",19],["Maria",20],["João",23]]

#for i in range(1,5):

#    print(f"\n{grupo}")


banco_dados_nomes=[] 
banco_dados_idade=[]

for contador in range (0,3):
    banco_dados_nomes.append(str(input("Nome : ")))
    banco_dados_idade.append(int(input("Idade : ")))

for pessoa in banco_dados_nomes:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]}é maior de idade")
    else:
        print(f"{pessoa[0]}é menor de idade")

  


