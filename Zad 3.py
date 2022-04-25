# Zadatak 3
N, B, lista = [], 0, []  # inicijalizacija varijabli


def RekUp(zbroj, i):  # algoritam rekurzivnog zbrajanja
    if(zbroj == B):
        lista.append(i)
        return
    if(zbroj > B):
        return
    if(zbroj < B):
        for broj in N:
            RekUp(zbroj + broj, i + 1)


def Ispis():  # definicija ispisa
    lista = []
    RekUp(0, 0)
    print("input: N =", N, ", B =", B)
    if len(lista) == 0:
        print("output: -1")
    else:
        print("output:", min(lista))
    print("\n")


def Test(n):
    if n == 1:  # test 1
        N = [2, 5, 1, 15]
        B = 11

    if n == 2:  # test 2
        N = [2, 5, 1, 4, 6]
        B = 5

    if n == 3:  # test 3
        N = [2, 4, 5]
        B = 3
    Ispis()


# Pozivanje metode
Test(1)
Test(2)
Test(3)
