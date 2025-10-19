def linhas ():
    print("="*30)

    print("Contagem de 1 ate 10 de 1 em 1")
    for i in range(1,11,1):
        print(f"{i}", end=' ')

    print()

    print("Contagem de 10 ate 0 de 2 em 2")
    for i in range (10,-1,-2):
        print(f"{i}", end=" ")


    print("Agora é a sua vez")
    inicio = int(input("inicio:"))
    fim = int(input("Final : "))
    passos = int(input("Passos : "))

    for i in range(inicio,fim,passos):
        print(f"{i}",end=" ")

linhas()