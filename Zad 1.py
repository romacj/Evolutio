import random


def Izbor():
    return random.randint(0, 2)


igrac = Izbor()
racunalo = Izbor()


def Igra(x, y):
    if(x == y):
        return "izjednačeno"
