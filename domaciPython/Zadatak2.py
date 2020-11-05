import math


def unosSekundi():
    a = input("Unesite sekundu od 0 - 86400 : ")
    return a

def racunanjeVremena(a):
     c = a/3600
     o = math.floor(c)
     n = a - o*3600
     l = n/60
     s = math.floor(l)
     f = n - s*60
     print(o, " : ", s, " : ", f)

a =  int (unosSekundi())
racunanjeVremena(a)
