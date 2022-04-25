import random


def Izbor():
    return random.randint(0, 2)


def Igra(x, y):
    if(x == y):
        return "Neodlučeno"
    if((x == 0 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 0)):
        return "Pobjeda igrača"
    else:
        return "Pobjeda računala"


def Naziv(x):
    if(x == 0):
        return "Kamen"
    if(x == 1):
        return "Škare"
    if(x == 2):
        return "Papir"


def Ispis():
    igrac = Izbor()
    racunalo = Izbor()
    print("Igrač:", Naziv(igrac))
    print("Računalo:", Naziv(racunalo))
    print(Igra(igrac, racunalo))


Ispis()
