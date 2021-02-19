
Hoteli = [
    {"Naziv": "Putnik", "Broj zvezdica": "3", "Adresa": "Ilije Ognjanovica 24", "Grad": "Novi Sad"},
    {"Naziv": "Sheraton", "Broj zvezdica": "4", "Adresa": "Polgar Andrasa 1", "Grad": "Novi Sad"},
    {"Naziv": "Vozarev", "Broj zvezdica": "3", "Adresa": "Pop Stojanova 16", "Grad": "Beograd"},
    {"Naziv": "Majestic", "Broj zvezdica": "4", "Adresa": "Obilicev Venac 28", "Grad": "Beograd"},
    { "Naziv": "Lotos", "Broj zvezdica": "3", "Adresa": "Vojvode Misica", "Grad": "Nis"}]


def meni():

    print("1. Dodajte novi hotel\n"
          "2. Ispis svih hotela\n"
          "E, Exit")



class Hotel:
    def __init__(self, naziv, adresa, grad):
        self.naziv = naziv
        self.adresa = adresa
        self.grad = grad
    def __str__(self):
        return f"naziv: {self.naziv}" \
               f"adresa: {self.adresa}" \
               f"grad: {self.grad}"

class hotel1(Hotel):
    def __init__(self, zvezdice):
        Hotel.__init__(self)
        self.zvezdice = zvezdice

    def __str__(self):
        return f"naziv: {self.naziv}, adresa: {self.adresa}, broj zvezdca: {self.zvezdice}, grad: {self.grad}"

    def dodaj_hotel (self):
        self.naziv = input("Ime hotela: ")
        self.grad = input("Grad u kom se nalazi: ")
        self.zvezdice = input("Broj zvezdica ")
        self.adresa = input("Adresa")
        Hoteli.append({"Naziv": self.naziv, "Adresa": self.adresa, "Broj zvezdica": self.zvezdice, "Grad": self.grad})


if __name__ == '__main__':
    while True:
        meni()

        izbor=input("")

        if izbor == '1':
            f = hotel1
            hotel1.dodaj_hotel(f)
            print("Uspesno ste dodali hotel", end='\n')
        elif izbor == '2':
            i = 0
            for a in Hoteli:
                print(Hoteli[i], end='\n')
                i = i + 1
        elif izbor == 'e':
            print("kraj")
            break
        else:
            print("Pogresno ste uneli, morate ponovo")