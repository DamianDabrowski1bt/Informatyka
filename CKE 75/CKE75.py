with open('tekst.txt') as plik:
    linia_tekstu = plik.readline()

print(linia_tekstu)
wyrazy = linia_tekstu.split()
print(wyrazy)

for wyraz in wyrazy:
    if wyraz[0] == 'd' and wyraz[-1] == 'd':
        print(wyraz)

def szyfr(napis, a, b):
    wynik = ""
    for znak in napis:
        kod = ((ord(znak) - 97) * a + b) % 26
        wynik += chr(kod + 97)
    return wynik

for wyraz in wyrazy:
    if len(wyraz) >= 10:
        print(szyfr(wyraz, 5, 2))

with open("probka.txt") as plik:
    for linia in plik:
        para = linia.split()
        for a in range(26):
            for b in range(26):
                if szyfr(para[0], a, b) == para[1]:
                    print(para, a, b)
                    break
        for a in range(26):
            for b in range(26):
                if szyfr(para[1], a, b) == para[0]:
                    print(para, a, b)
                    break
