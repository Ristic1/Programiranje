#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int jednaki(char *s1, char *s2){
    int a;

            a=strcmp(s1, s2);

    return a;


}


int main()
{   int a;

    char string[20];
    char string1[20];
    printf("Unesi string:\n");
    gets(string);
    printf("Unesi string:\n");
    gets(string1);
    a=jednaki(string, string1);
    if(a==0)
        printf("Stringovi su indenticni\n");
    else
        printf("Stringovi su razliciti\n");


    return 0;
}

