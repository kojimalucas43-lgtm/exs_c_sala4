#include <stdio.h>
#include <string.h>
#include <ctype.h>
 
// Remove caracteres não numéricos e retorna o tamanho
int limpar_cpf(const char *entrada, char *saida) {
    int j = 0;
    for (int i = 0; entrada[i] != '\0'; i++) {
        if (isdigit(entrada[i])) {
            saida[j++] = entrada[i];
        }
    }
    saida[j] = '\0';
    return j;
}
 
// Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
int todos_iguais(const char *cpf) {
    for (int i = 1; i < 11; i++) {
        if (cpf[i] != cpf[0]) return 0;
    }
    return 1;
}
 
// Valida o CPF e retorna 1 se válido, 0 se inválido
int validar_cpf(const char *cpf_entrada) {
    char cpf[12];
    int tamanho = limpar_cpf(cpf_entrada, cpf);
 
    // Deve ter exatamente 11 dígitos
    if (tamanho != 11) return 0;
 
    // Rejeita sequências com todos os dígitos iguais
    if (todos_iguais(cpf)) return 0;
 
    // --- Cálculo do 1º dígito verificador ---
    int soma = 0;
    for (int i = 0; i < 9; i++) {
        soma += (cpf[i] - '0') * (10 - i);
    }
    int resto = (soma * 10) % 11;
    if (resto == 10 || resto == 11) resto = 0;
    if (resto != (cpf[9] - '0')) return 0;
 
    // --- Cálculo do 2º dígito verificador ---
    soma = 0;
    for (int i = 0; i < 10; i++) {
        soma += (cpf[i] - '0') * (11 - i);
    }
    resto = (soma * 10) % 11;
    if (resto == 10 || resto == 11) resto = 0;
    if (resto != (cpf[10] - '0')) return 0;
 
    return 1;
}
 
// Formata o CPF no padrão XXX.XXX.XXX-XX
void formatar_cpf(const char *cpf, char *formatado) {
    sprintf(formatado, "%c%c%c.%c%c%c.%c%c%c-%c%c",
        cpf[0], cpf[1], cpf[2],
        cpf[3], cpf[4], cpf[5],
        cpf[6], cpf[7], cpf[8],
        cpf[9], cpf[10]);
}
 
int main() {
    char entrada[30];
    char cpf_limpo[12];
    char cpf_formatado[15];
 
    printf("=============================\n");
    printf("   VALIDADOR DE CPF em C\n");
    printf("=============================\n");
    printf("Digite o CPF (com ou sem formatacao): ");
    scanf("%29s", entrada);
 
    int tamanho = limpar_cpf(entrada, cpf_limpo);
 
    printf("\n-----------------------------\n");
    printf("CPF informado : %s\n", entrada);
 
    if (tamanho == 11) {
        formatar_cpf(cpf_limpo, cpf_formatado);
        printf("CPF formatado : %s\n", cpf_formatado);
    }
 
    printf("Resultado     : ");
 
    if (validar_cpf(entrada)) {
        printf("VALIDO ✔\n");
    } else {
        printf("INVALIDO ✘\n");
    }
 
    printf("-----------------------------\n");
 
    return 0;
}