#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "portuguese");


    char cidade[50];
    char estado[50];
    int ano;
    int resp;

    printf("Digite sua cidade: ");
    fgets(cidade, 50, stdin);

    printf("Digite seu estado: ");
    fgets(estado, 50, stdin);

    printf("Ano de nascimento: ");
    scanf("%d", &ano);

    resp = 2026 - ano;

    printf("A cidade de %s, no estado de %s tem %d anos \n\n", cidade, estado, resp);


    system("pause");
    return 0;
}
