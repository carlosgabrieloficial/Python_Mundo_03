from datetime import datetime

dados = {}

dados["Nome"] = str(input("Nome :"))
nascimento = int(input("Nascimento"))
dados["idade"] = datetime.now().year - nascimento
dados['CTPS']  = int(input("Carteira de Trabalho : [0 se não tiver]"))
if dados["CTPS"] != 0 :
    dados["CONTRATAÇÃO"] = int(input("ANO DE CONTRATAÇÃO"))
    dados["Salario"] = float(input("Salario R$:"))
    dados["Aposentadoria"] = dados["idade"] + ((dados["CONTRATAÇÃO"] + 35 ) - datetime.now().year)
print("=-"*30)

for key, value in dados.items():
    print(f"{key} tem o valor {value}")