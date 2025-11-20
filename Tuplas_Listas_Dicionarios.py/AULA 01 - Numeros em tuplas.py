
lista = ("zero","um","dois","tres","quadro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quartoze","quinze","dizeies","dezsete","dezoito","dezenove","vinte")

while True:
    num = int(input('de 0 ate 20 :'))
    if 0 <= num <= 20 :
        break

    
    resposta = " "
    while resposta not in "NS" :
        resposta = str(input("Quer continuar [N/S] : ")).strip().upper()[0]
    if resposta == "N":
        break


print(f"{lista[num]}")
