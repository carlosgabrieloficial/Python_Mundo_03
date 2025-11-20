def contador (inicio, final, passo ):

    print(f"Contagem de {inicio} ate {final} de {passo} em {passo}")

    if passo < 0 :
        passo *= -1

    if passo == 0:
        passo = 1


    if inicio < final :
        contador = inicio

        while contador <= final :
            print(f"{contador}",end=" ")
            contador += passo
        print()
    

    
    else:
        contador = inicio 

        while contador >= final :
            print(f"{contador}",end=" ")
            contador -= passo
        print()


contador(1,10,1)
contador(10,0,1)



inic = int(input("Valor inicial")) 
fina = int(input("Valor final"))
pas = int(input("Passo :"))

contador(inic,fina,pas)


