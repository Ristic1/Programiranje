import random


class Libr:
    def __init__(self, naziv):
        self.naziv = naziv
        self.knjige = []


    def info(self):
        knjige = []
        f = open("knjiga.txt", "r")
        lines = f.readlines()
        for i in lines:
            a = i.split("|")
            knjige.append(a[1])
        self.knjige = knjige
        f.close()
        print("Ime biblioteke: " + self.naziv)
        print("Nazivi knjiga: ")
        for i in self.knjige:
            print("" + i)
        knjige.clear()


class Knjiga:
    def __init__(self, naslov, autor, zanr, biblioteka):
        self.__get_isbn()
        self.naslov = naslov
        self.autor = autor
        self.zanr = zanr
        self.biblioteka = biblioteka
        self.file()


    def __get_isbn(self):
        self.isbn = random.randint(1, 100)
        f = open("knjiga.txt", "r")
        lines = f.readlines()
        for i in lines:
            x = i.split("|")
            while int(x[0]) == self.isbn:
                self.isbn = random.randint(1, 100)
        f.close()


    def file(self):
        f = open("knjiga.txt", "a")
        f.write(str(self.isbn) + "|" + self.naslov + "|" + self.autor + "|" + self.zanr + "|" + self.biblioteka.naziv + "\n")
        f.close()

def menu():
    print("1. Dodavanje knjige")
    print("2. Podaci o biblioteci")
    print("3. Info o knjizi")
    print("4. KRAJ")


def dodatiKnjigu(biblioteka):
    naslov = input("Ime knjige: ")
    autor = input("Autor: ")
    zanr = input("Zanr: ")
    novaKnjiga = Knjiga(naslov, autor, zanr, biblioteka)


def podaciKnjige():
    knjige = []
    f = open("knjiga.txt", "r")
    lines = f.readlines()
    f.close()
    for i in lines:
        a = i.split("|")
        knjige.append(a[0])
    print(knjige)
    isbn = input("Unos isbn: ")
    while isbn not in knjige:
        isbn = input("Unesite ponovo ako pogresite")
    knjige.clear()
    for i in lines:
        a = i.split("|")
        if isbn == a[0]:
            print(
                "Naslov| " + a[1] + "|" + " Autor| " + a[2] + "|" + " Zanr|" + a[3] + "|" +  "Biblioteka: " + a[4])


if __name__ == '__main__':
    libr1 = "NoviSad"
    libr = Libr(libr1)
    while True:
        menu()
        n = input("Unesite broj opcije: ")
        if int(n) == 1:
            dodatiKnjigu(libr)

        elif int(n) == 2:
            libr.info()

        elif int(n) == 3:
            podaciKnjige()

        elif int(n) == 4:
            quit()

        elif int(n) < 1 or int(n) > 4:
            print("Pogresno ste uneli!")