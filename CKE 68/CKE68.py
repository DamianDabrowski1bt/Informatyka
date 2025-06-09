def jednolity(ciag):
    for i in range(len(ciag) - 1):
        if ciag[i] != ciag[i+1]:
            return False
    return True

lista_napisow = []
with open("dane_napisy.txt") as plik:
    for linia in plik:
        lista_napisow.append(linia.split())

licznik = 0
for para in lista_napisow:
    if para[0] == para[1]:
        if jednolity(para[0]):
            licznik += 1
print(licznik)
licznik = 0

for para in lista_napisow:
    if sorted(para[0]) == sorted(para[1]):
        licznik += 1
print(licznik)

lista_napisow = []
with open("dane_napisy.txt") as plik:
    for linia in plik:
        a, b = linia.strip().split()
        lista_napisow.append(a)
        lista_napisow.append(b)

slownik_anagramow = {}

for ciag in lista_napisow:
    klucz = ''.join(sorted(ciag))
    if klucz not in slownik_anagramow:
        slownik_anagramow[klucz] = []
    slownik_anagramow[klucz].append(ciag)

maks = max(len(wartosc) for wartosc in slownik_anagramow.values())
print(maks)
