def kombinovani_String():
    str1 = input("Unesite prvu rec koja mora imati vise od 3 karaktera: ")
    str2 = input("Unesite drugu rec koja mora imati vise od 3 karaktera: ")
    str_prvi = str1[0:3]
    str_kraj = str2[-3:]
    kombinovan_string = str_prvi + str_prvi + str_kraj
    print(kombinovan_string)

if __name__ == '__main__':
    kombinovani_String()