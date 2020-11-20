def akronim_Fraze():
    fraza = input("Unesite neku frazu: ")
    f = fraza.split()
    akronimFraze = ""
    for i in f:
        akronimFraze = akronimFraze + i[0].upper()

    print("Akronim unete fraze je ", akronimFraze)

if __name__ == '__main__':
    akronim_Fraze()