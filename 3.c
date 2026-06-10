#include <stdio.h>

int main() {
    int numero, i;

    printf("Digite um numero: ");
    scanf("%d", &numero);

    printf("\nTabuada do 9:\n");

    for (i = 1; i <= numero; i++) {
        printf("9 x %d = %d\n", i, 9 * i);
    }


    system("pause");
    return 0;
}