#include <stdio.h>
#include <stdlib.h>

int main()
{
   int n, j, i;
   printf("Unesite dimenziju kvadratne matrice: ");
   scanf("%d", &n);
   printf("\n________________\n\n");

   int niz[n][n];

   printf("Unesite elemente matrice: \n");
   for(i=0;i<n;i++){
    for(j=0;j<n;j++){
            printf("[%d][%d] element:\n",i,j );
            scanf("%d", &niz[i][j]);

    }
}   printf("Ispis:\n");
   for(i=0;i<n;i++){
    for(j=0;j<n;j++){
           printf("%d",niz[i][j]);



    }printf("\n");
}
    int a;
   for(i=0;i<n;i++){
    for(j=0;j<n;j++){
            if(i<j){
                a=niz[i][j];
               niz[i][j]=niz[j][i];
                niz[j][i]=a;
            }
    }
   }



   printf("Ispis nakon promene:\n");
   for(i=0;i<n;i++){
    for(j=0;j<n;j++){
           printf("%d",niz[i][j]);



    }printf("\n");
}





    return 0;
}
