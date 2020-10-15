#include <stdio.h>
#include <stdlib.h>


int main()
{
    FILE *f1;
    FILE *f2;
    f1=fopen("file1.txt", "w+");
    f2=fopen("file2.txt", "w+");
    printf("Unesite tekst koji je u prvom fajlu \n");
    char rec1[100];
    gets(rec1);
    fprintf(f1,"%s",rec1);
    fflush(stdout);
    char rec2[100];
    printf("Unesite tekst koji je u drugom fajlu \n");
    gets(rec2);
    fprintf(f2,"%s",rec2);
    fflush(stdout);
    FILE *f3;
    f3=fopen("file3.txt", "w+");
    fprintf(f3,"%s %s",rec1,rec2);
    fflush(stdout);
    fclose(f1);
    fclose(f2);
    fclose(f3);
    return 0;











    return 0;
}
