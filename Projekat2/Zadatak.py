listaReci = {}


def menu():
    print("************************")
    print("-_-_MENI_-_-")
    print("1. Unos reci")
    print("2. Brisanje reci ")
    print("3. Izmena reci ")
    print("4. Ispis reci ")
    print("5. Kraj programa ")
    print("************************")


def unos():
    print("Unos : ")
    redniBroj = input("Unesite redni broj")
    ime = input(" Unesite ime: ")
    listaReci[redniBroj] = ime
    print(listaReci)


def uklanjanje():
    uklanjanje = input("Unesite broj koji zelite da uklonite")
    listaReci.pop(uklanjanje)
    print(listaReci)


def izmena():
    redniBroj = input("Unesite broj koji cete izmeniti: ")
    izmena = input("Unesite novo ime: ")
    listaReci[redniBroj] = izmena
    print(listaReci)


def ispis():
    for redniBroj, ime in listaReci.items():
        print(redniBroj, ime)


if __name__ == '__main__':
    while True:
        menu()

        f = input("---")

        if f == '1':
            unos()
        elif f == '2':
            uklanjanje()
        elif f == '3':
            izmena()
        elif f == '4':
            ispis()
        elif f == "5":
            break