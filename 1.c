#include <stdio.h>

int main() {
    char nome[50];
    int numero;

    // Solicita o nome
    printf("Digite o seu nome: ");
    scanf("%49s", nome);

    // Solicita o número
    printf("Digite um numero inteiro: ");
    scanf("%d", &numero);

    printf("\nOla, %s!\n", nome);

    // Verifica a condição do número
    if (numero <= 45) {
        printf("O numero e menor que 45. Aqui esta uma girafa:\n\n");
        printf("            @@@@      \n");
        printf("           @    @     \n");
        printf("           @    @     \n");
        printf("            @  @      \n");
        printf("             @@  <-- cabecinha\n");
        printf("             ||       \n");
        printf("             ||  <--- pescocao\n");
        printf("             ||       \n");
        printf("             ||       \n");
        printf("             ||       \n");
        printf("          ---||---    \n");
        printf("         /   ||   \\   \n");
        printf("        @    ||    @  \n");
        printf("       / \\   ||   / \\ \n");
        printf("      /   \\ /  \\ /   \\\n");
        printf("     @     @    @     @\n");
        printf("     |     |    |     |\n");
        printf("    ===   ===  ===   ===\n");
        printf("\n  ~~ GIRAFA ~~\n\n");
    } else {
        printf("O numero e 45 ou maior. Aqui esta um rinoceronte:\n\n");
        printf("          /@           \n");
        printf("         /  @          \n");
        printf("        /  /  <-- chifrao\n");
        printf("       / /             \n");
        printf("   @@@@@@@@@@@@        \n");
        printf("  @              @     \n");
        printf(" @   o        o   @    \n");
        printf(" @                @    \n");
        printf("  @    ________  @     \n");
        printf("   @            @      \n");
        printf("    @@@@@@@@@@@@       \n");
        printf("    |  |      |  |     \n");
        printf("    |  |      |  |     \n");
        printf("   ====      ====      \n");
        printf("\n  ~~ RINOCERONTE ~~\n\n");
    }


    system("pause");
    return 0;
}