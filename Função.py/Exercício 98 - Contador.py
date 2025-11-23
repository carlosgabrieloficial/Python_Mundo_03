##Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

#=====================================================================================================

#ALUNO

def contador(i,f,p):

    if p == 0 :
        p = 1

    print("="*30)
    print(f"Inicio:{i}, Final:{f}, Passo:{p}")
    print("="*30)

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ")
            cont += p
        print("FIM")
    
    else:
        cont = i 
        while cont >= f:
            print(f"{cont}", end=" ")
            cont -= p
        print("FIM")

contador(10,0,1)
contador(0,20,2)

print("SUA VEZ")
numero1= int(input("Inicio : "))
numero2= int(input("Final : "))
numero3= int(input("Passo : "))

contador(numero1,numero2,numero3)