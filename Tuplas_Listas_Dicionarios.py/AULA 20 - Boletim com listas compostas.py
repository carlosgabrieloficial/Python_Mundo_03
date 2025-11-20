alunos = []

while True:

    nome_aluno  = str(input("Nome do aluno: "))
    nota1_aluno = float(input("Nota 1: "))
    nota2_aluno = float(input("Nota 2: "))
    media_aluno = (nota1_aluno + nota2_aluno) / 2 

    alunos.append([nome_aluno,[nota1_aluno,nota2_aluno],media_aluno])

    continua = str(input("Quer continuar [S/N] ? "))
    if continua in "Nn":
        break

print("=-"*20)
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("=-"*20)

for i , a in enumerate (alunos): 
    print(f"{i:<4}{a[0]:10}{a[2]:>8.1f}")

while True:
    opcao = int(input("Mostrar notas de qual aluno ? [digite 999]"))
    if opcao == 999 :
        print("FIM DO PROGRAMA")
        break
    if opcao <= len(alunos) - 1 :
        print(f"{alunos[opcao][0]}","são "  f"{alunos[opcao][1]}")