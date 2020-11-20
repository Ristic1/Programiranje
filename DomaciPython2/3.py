def meni():
    print("1. restart")
    print("2. end")


if __name__ == '__main__':

 while True:

    name = input("username:")
    password = input("password:")
    file = open("korisnici.txt", "a")
    file.write(name)
    file.write("|")
    file.write(password)
    file.write("\n")
    print("Unos u vas fajl je uspeo")
    file.close()
    meni()
    f = input("Option>>>")
    if f == '2':
        break
