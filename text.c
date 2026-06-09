#include <stdio.h>
#include <stdlib.h>

int main(){

   char nome[50];
   printf("Digite um nome: ");
   //scanf("%s", nome);
   fgets(nome,50, stdin);

   printf("\nO nome informado foi: %s \n", nome);


    system("pause");
    return 0;
}
