#include <stdio.h>

int main() {
    int numero, i;

    printf("Digite um numero: ");
    scanf("%d", &numero);

    printf("\nTabuada do 7:\n");

    for (i = 1; i <= numero; i++) {
        printf("7 x %d = %d\n", i, 7 * i);
    }


    system("pause");
    return 0;
}