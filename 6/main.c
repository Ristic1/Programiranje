#include <stdio.h>
#include <stdlib.h>

void unosMatrica(int** niz){
     int p=0,i,j;
        printf("Unesite brojeve u matricu \n");
        for(i=0;i<3;i++){
            for(j=0;j<3;j++){
                scanf("%d",(niz+p));
                p+=4;
            }
        printf("\n");
        }



}


void ispisMatrica(int** niz){
     int p=0,i,j;
        for(i=0;i<3;i++){
            for(j=0;j<3;j++){
                printf("%d",*(niz+p));
                p+=4;
            }
        printf("\n");
        }




}


void sabiranjeMatrica(int *niz, int *niz1){
    int p=0,i,j;
        for(i=0;i<3;i++){
            for(j=0;j<3;j++){
                printf("%d ",*(niz+p) +  *(niz1+p));
                p+=4;
            }
        printf("\n");
        }




}










int main()
{
int niz[3][3];
int niz1[3][3];

unosMatrica(niz);
printf("\n---------------\n");
unosMatrica(niz1);
printf("\n---------------\n");
ispisMatrica(niz);
printf("\n---------------\n");
ispisMatrica(niz1);
printf("\n---------------\n");
sabiranjeMatrica(niz,niz1);
printf("\n---------------\n");


    return 0;
}
