from random import randint

numero = randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10)

for numeros in numero :
    print(numeros , end=" ")
print (f"\nMAIOR {max(numero)}")
print (f"\nMENOR {min(numero)}")
