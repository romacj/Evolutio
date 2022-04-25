def Rek(x, y, txt):
    if(txt[x] != txt[y]):
        print("Nije palindrom")
        return
    else:
        if(y < x):
            print("Palindrom")
            return
        else:
            if(txt[x] == txt[y]):
                Rek(x+1, y-1, txt)


def tekstFormat(txt):
    txt0 = ""
    for znak in txt:
        if znak.isalpha():
            txt0 += znak
    return txt0.lower()


def Test(n):
    if(n == 1):
        tekst = "A mene tu, ni minute nema"
    if(n == 2):
        tekst = "Trka automobila"
    print(tekst)
    tekst = tekstFormat(tekst)
    Rek(0, len(tekst)-1, tekst)


Test(1)
Test(2)
