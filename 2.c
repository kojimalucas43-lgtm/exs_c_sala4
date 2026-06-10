#include <stdio.h>

int main() {
    int altura, i, j, k;

    // Solicita a altura da pirâmide ao usuário
    printf("Digite a altura da piramide: ");
    scanf("%d", &altura);

    printf("\nAqui esta a sua piramide:\n\n");

    // Loop externo: controla a linha atual
    for (i = 1; i <= altura; i++) {
        
        // Primeiro loop interno: imprime os espaços para alinhar a pirâmide
        for (j = 1; j <= altura - i; j++) {
            printf(" ");
        }

        // Segundo loop interno: imprime os asteriscos
        // A lógica (2 * i - 1) garante uma quantidade ímpar de asteriscos por linha (1, 3, 5, 7...)
        for (k = 1; k <= (2 * i - 1); k++) {
            printf("*");
        }

        // Pula para a próxima linha
        printf("\n");
    }
 

    system("pause");
    return 0;
}