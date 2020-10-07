#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int provera(char *s1, char c){
    int i;
    int j=0;
    for(i=0;i<=strlen(s1);i++){
       if(s1[i]==c)
        j++;


    }
    return j;



}





int main()
{   int a;
    char c='a';
    char rec[20]="StaStaStaSta";
    printf("%d\n\n\n", strlen(rec));
    a=provera(rec, c);
    printf("Ponavlja se %d puta\n",a);












    return 0;
}
