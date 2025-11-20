from datetime import datetime

hoje_agora = datetime.now().year


banco_dados = {}

banco_dados["Nome"] = str(input("Digite o seu nome :"))
banco_dados["Nacismento"] = int(input("Ano de nacismento :"))
idade = hoje_agora - banco_dados["Nacismento"]


banco_dados["Carteira de Trabalho (0 não tem)"] = int(input("Numero da carteira de trabalho [0,para sair]"))

if banco_dados["Carteira de Trabalho (0 não tem)"] == 0 :
    print("FIM DO PROGRAMA")
    exit()

banco_dados["Ano de contratação"] = int(input("Ano de contração :"))

banco_dados["Salario"] = float(input("Salario : "))


print("-="*30)

print(f" - O nome tem o valor de {banco_dados['Nome']}")
print(f" - A idade tem o valor de {idade}")
print(f" - A CTPS tem o valor de {banco_dados['Carteira de Trabalho (0 não tem)']}")
print(f" - A Contração tem o valor de {banco_dados['Ano de contratação']}")
print(f" - O Salario tem o valor de {banco_dados['Salario']}")
print(f" - Falta tem {65-idade} anos para se aposentar")







