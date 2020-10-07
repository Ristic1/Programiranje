#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{   int n;
    printf("Unesite broj elemenata niza\n");
    scanf("%d", &n);
   int niz[n];

   int *p=niz;
   int i;
   int a=0;
   for(i=0;i<n;i++){
    printf("Unesite %d. broj\n", i+1);
    scanf("%d", p+i);

   }

    for(i=0;i<n;i++){
       if(*(p+i)>a){
        a=*(p+i);
       }
    }

printf("Najveci broj je:%d\n", a);






    return 0;
}
