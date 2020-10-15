#include <stdio.h>
#include <stdlib.h>

int main()
{
  FILE *f;
    f=fopen("file1.txt", "w+");
    printf("Unesite tekst u datoteku:\n");
    char rec[100];
    gets(rec);
    fprintf(f, "%s", rec);
    fflush(stdin);
    brojReci(rec);
    najduzaRec(rec);
    fclose(f);




   //nisam stigao da uradim funkcije ali ako je neophodno uradicu naknadno//


    return 0;
}
