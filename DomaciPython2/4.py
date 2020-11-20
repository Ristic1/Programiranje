def ispis_Usera():
    file = open("korisnici.txt", "r")
    for line in file.readlines():
        user = line.split("|")
        username = user[0]
        password = user[1]
        print("Ime korisnika: " + username)
        print("Lozinka korisnika: " + password)
    file.close()


if __name__ == '__main__':
    ispis_Usera()