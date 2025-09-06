#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("aprender","programar","linguagem","python",
            "curso","gratis","video","rock")

for pal in palavras:

    print(f"\nNa palavra {pal}", end=" ")

    for letras in pal :
        if letras.lower() in "aeiou":
            print(letras, end=" ")
