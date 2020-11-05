meseci1 = ["januar", "mart", "maj", "jul", "avgust", "oktobar", "decembar"]
meseci2 = ["april", "jun", "septembar", "novembar"]


def unosMeseca():
    k = input('Unesite bilo koji mesec : ')
    return k

def proveraDana(mesec):
    if mesec in meseci1:
        print("Ovaj mesec " + mesec + " ima 31 dan")
        return 0
    if mesec in meseci2:
        print("Ovaj mesec " + mesec + " ima 30 dana")
        return 0
    else:
        print("Februar ima 28, 29 dana")
        return 0

mesec = unosMeseca()
proveraDana(mesec)
