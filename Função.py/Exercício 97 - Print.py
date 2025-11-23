#  Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#PROFESSOR

def mensagem(msg):

    tamanho = len(msg) + 4

    print("="*tamanho)
    print(f"  {msg}")



mensagem("carlos")
mensagem("gabriel")
mensagem("sousa")


