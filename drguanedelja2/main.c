#include <stdio.h>
#include <stdlib.h>
#include "zadatak.h"
int main()
{
   ucenik n;
FILE* f = fopen("PodaciDjaka.txt", "w");
char razmak[20] = "\n_______________\n";
printf("Unesite broj u dnevniku:\n");
gets(n.brojDnevnik);
fputs(n.brojDnevnik, f);
fputs(razmak, f);
printf("Unesite ime djaka:\n");
gets(n.ime);
fputs(n.ime, f);
fputs(razmak, f);
printf("Unesite prezime djaka:\n");
gets(n.prezime);
fputs(n.prezime, f);
fputs(razmak, f);
fclose(f);








    return 0;
}
//Ovo sam uradio sa .h fajlom samo da bih se podsetio tog dela gradiva//
