#include <stdio.h>
#include <stdlib.h>

int main()
{
FILE* f= fopen("PRIMER.txt", "w");
char tekstPrimer[100];
printf("Unesite tekst koji ce biti prikazan u file-u:\n");
gets(tekstPrimer);
fputs(tekstPrimer, f);
printf("Unesite karakter koji ce biti prebrojan:\n");
char c;
scanf("%c", &c);
fgets(tekstPrimer, 0, f);
fseek(f, 0, SEEK_SET);
int a=0;
for(int i=0; i<100; i++){
    if(c==tekstPrimer[i])
      a++;
}
fclose(f);
printf("Vas znak se u tekstu pojavio %d puta", a);

    return 0;
}
