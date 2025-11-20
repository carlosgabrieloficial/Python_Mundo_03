##  Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


nota_aluno ={"nome":" ", "media":" ","situação":" "}

nota_aluno["nome"] = input("Digite o seu nome:  ")

nota_aluno["media"] = float(input("Qual a sua nota: "))

if nota_aluno["media"] >= 7 :
    nota_aluno["situação"] = ("APROVADO")
else:
    nota_aluno["situação"] = ("RECUPERAÇÃO")

print("-="*30)
print()
print(f" - O nome do aluno é {nota_aluno['nome']}")
print()
print(f" - A media do aluno é {nota_aluno['media']}")
print()
print(f" - A situação do aluno é {nota_aluno['situação']}")
print()
print("FIM DO PROGRAMA")