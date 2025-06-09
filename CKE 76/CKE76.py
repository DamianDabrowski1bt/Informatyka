dane_szyfr1 = []
klucz_szyfr1 = None
with open('szyfr1.txt') as plik:
    for linia in plik:
        dane_szyfr1.append(linia.strip())
    klucz_szyfr1 = list(map(int, dane_szyfr1[-1].split()))
    dane_szyfr1.pop()

def szyfrowanie(klucz, tekst):
    znaki = list(tekst)
    n = len(klucz)
    for i in range(len(tekst)):
        poz = klucz[i % n] - 1
        znaki[i], znaki[poz] = znaki[poz], znaki[i]
    return ''.join(znaki)

for wyraz in dane_szyfr1:
    print(szyfrowanie(klucz_szyfr1, wyraz))

dane_szyfr2 = []
klucz_szyfr2 = None
with open('szyfr2.txt') as plik:
    for linia in plik:
        dane_szyfr2.append(linia.strip())
    klucz_szyfr2 = list(map(int, dane_szyfr2[-1].split()))
    dane_szyfr2.pop()

for wyraz in dane_szyfr2:
    print(szyfrowanie(klucz_szyfr2, wyraz))

def deszyfrowanie(klucz, tekst):
    znaki = list(tekst)
    n = len(klucz)
    for i in range(len(tekst) - 1, -1, -1):
        poz = klucz[i % n] - 1
        znaki[i], znaki[poz] = znaki[poz], znaki[i]
    return ''.join(znaki)

szyfr3_tekst = None

with open('szyfr3.txt') as plik:
    szyfr3_tekst = plik.readline().strip()

print(szyfr3_tekst)

odszyfrowany = deszyfrowanie([6, 2, 4, 1, 5, 3], szyfr3_tekst)
print(odszyfrowany)
