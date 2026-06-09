//Inclui a biblioteca stdio.h que permite usar entrada e saída de infos(printf)
#include <stdio.h>
//Inclui bibliotecas utilitarias (system())
#include <stdlib.h>

int main(){

    //declara variavel
    float numero1, numero2, resp;

    printf("Digite o primeiro número: ");
    scanf("%f", &numero1);
    printf("Digite o segundo número: ");
    scanf("%f", &numero2);
    resp = numero1 + numero2;
    printf("%.2f", resp);



    //pausa o sistema ate que seja pressionado uma tecla
    system("pause");
    //finalizando o sist
    return 0;
}
