#include <stdio.h>
#include <stdlib.h>

int main()
{
   int n;
    printf("Unesite broj elemenata niza\n");
    scanf("%d", &n);
   int niz[n];
   int *p=niz;
   int i;


   for(i=0;i<n;i++){
    printf("Unesite %d. broj\n", i+1);
    scanf("%d", p+i);

   }int j=1;
   for(i=0;i<n;i++){
    if(*(p+i)%3==0){
       printf("%d. broj:%d\n",j, *(p+i));
       ++j;
    }


   }





    return 0;
}
