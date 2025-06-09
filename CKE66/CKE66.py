def sumaCyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma

def first(liczba):  # liczba jest typu int
    if liczba < 2:
        return False
    elif liczba == 2:
        return True
    elif liczba % 2 == 0:
        return False
    for i in range(3, int(liczba**0.5), 2):
        if liczba % i == 0:
            return False
    return True

lista_trojek = []
with open("trojki.txt") as file:
    for linia in file:
        lista_trojek.append(linia.split())

for liczby in lista_trojek:
    if sumaCyfr(liczby[0]) + sumaCyfr(liczby[1]) == int(liczby[2]):
        print(liczby)

for liczby in lista_trojek:
    if int(liczby[0]) * int(liczby[1]) == int(liczby[2]):
        if first(int(liczby[0])) and first(int(liczby[1])):
            print(liczby)
