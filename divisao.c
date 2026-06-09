#include <stdio.h>
#include <stdlib.h>

int main(){

    float numero1, numero2, resp;

    printf("Digite o primeiro número: ");
    scanf("%f", &numero1);
    printf("Digite o segundo número: ");
    scanf("%f", &numero2);

    if(numero1 !=0 && numero2!=0){
    resp = numero1 / numero2;
    printf("%.2f", resp);
    } else{
        printf("Não da pra dividir por 0 desgraçado");
    }



    system("pause");
    return 0;
}
