def RekUp(zbroj, i, N, B, lista):
    if(zbroj == B):
        lista.append(i)
        return
    if(zbroj > B):
        return
    if(zbroj < B):
        for broj in N:
            RekUp(zbroj + broj, i + 1, N, B, lista)


def Test(n):
    if n == 1:
        N = [2, 5, 1, 15]
        B = 11

    if n == 2:
        N = [2, 5, 1, 4, 6]
        B = 5

    if n == 3:
        N = [2, 4, 5]
        B = 3

    lista = []
    RekUp(0, 0, N, B, lista)
    print("N =", N, ", B =", B)
    if len(lista) == 0:
        print("-1")
    else:
        print(min(lista))


Test(1)
Test(2)
Test(3)
