def unos():
    a = input("Unesite broj od kog ce biti nadjen faktorijel ")
    return a

def faktorijel(a):
    f = 1
    while a != 0:
        f*=a
        a-=1
    return f

a = int (unos())
print("Faktorijel je: ", faktorijel(a))
