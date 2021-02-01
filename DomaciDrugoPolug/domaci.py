class krug:
    def __init__(self, poluprecnik):
        self.poluprecnik = poluprecnik
    def okruga(self, obim):
        return f"Obim kruga je {obim}"
    def pkruga(self, povrsina):
        return f"Povrsina kruga je {povrsina}"

class kvadrat:
    def __init__(self, c):
        self.c = c
    def okvad(self, obim):
        return f"Obim kvadrata je {obim}"
    def pkvad(self, povrsina):
        return f"Povrsina kvadrata je {povrsina}"

class pravougaonik:
    def __init__(self, c, f):
        self.c = c
        self.f = f
    def oprav(self, obim):
        return f"Obim pravougaonika je {obim}"
    def pprav(self, povrsina):
        return f"Povrsina pravougaonika je {povrsina}"



if __name__ == '__main__':
    polup = float(input("Unesite poluprecnik kruga: "))
    krug = krug(polup)
    obimkruga = (2*krug.poluprecnik)*3.14
    print(krug.okruga(obimkruga))
    povrsinakruga = (krug.poluprecnik*krug.poluprecnik)*3.14
    print(krug.pkruga(povrsinakruga))

    c = float(input("Unesite stranicu kvadrata: "))
    kvadrat = kvadrat(c)
    obimkv = 4 * kvadrat.c
    print(kvadrat.okvad(obimkv))
    povrsinakv = kvadrat.c * kvadrat.c
    print(kvadrat.pkvad(povrsinakv))

    c = float(input("Unesite jednu stranicu pravouganika (c): "))
    f = float(input("Unesite drugu stranicu pravouganika (f): "))
    pravougaonik = pravougaonik(c, f)
    obimp = 2*(pravougaonik.c+pravougaonik.f)
    print(pravougaonik.oprav(obimp))
    povrsinaprav = pravougaonik.c*pravougaonik.f
    print(pravougaonik.pprav(povrsinaprav))


