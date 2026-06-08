# Pesquisa em C


## Introdução

A linguagem C foi criada entre na década de 70 por **Dennis Ritchie** nos laboratórios Bell Labs. Ela foi criada na necessidade de reescrever o sistema operacional Unix em uma linguagem de alto nível portável. Antes dela, sistemas operacionais eram escritos em assembly — código específico para cada hardware. O C resolveu isso: oferecia controle de baixo nível com a expressividade de uma linguagem estruturada.

Suas principais características são:

- **Eficiência**: compilada diretamente para código de máquina
- **Portabilidade**: um programa C pode ser recompilado para diferentes arquiteturas
- **Controle**: acesso direto à memória via ponteiros
- **Simplicidade**: conjunto pequeno de palavras-chave (apenas 32 no padrão C89)

O padrão mais utilizado hoje é o **C99** e o **C11**, definidos pela ISO/ANSI. O C é a base de linguagens como C++, Java, C#, Go e Rust.

---

##  Estrutura Básica

Todo programa em C segue uma estrutura mínima:

```c
#include <stdio.h>   // Inclui biblioteca padrão de entrada/saída

int main() {
    printf("Olá, Mundo!\n");
    return 0;        // Retorna 0 ao sistema operacional (sucesso)
}
```

### Elementos fundamentais

| Elemento        | Descrição                                              |
|-----------------|--------------------------------------------------------|
| `#include`      | Diretiva de pré-processador para incluir cabeçalhos    |
| `main()`        | Ponto de entrada obrigatório do programa               |
| `printf()`      | Função de saída formatada (biblioteca `stdio.h`)       |
| `;`             | Terminador de instrução                                |
| `{ }`           | Delimitadores de bloco de código                       |

### Tipos de Dados Primitivos

```c
int    x = 10;        // Inteiro (tipicamente 4 bytes)
float  f = 3.14;      // Ponto flutuante simples
double d = 3.14159;   // Ponto flutuante dupla precisão
char   c = 'A';       // Caractere (1 byte)
void               ;  // Ausência de tipo (usado em funções/ponteiros)
```

Modificadores: `short`, `long`, `unsigned`, `signed` alteram tamanho e intervalo dos tipos.

---

## Controle de Fluxo

### Condicionais

```c
if (x > 0) {
    printf("Positivo\n");
} else if (x < 0) {
    printf("Negativo\n");
} else {
    printf("Zero\n");
}

// Switch para múltiplos casos
switch (opcao) {
    case 1: printf("Um\n"); break;
    case 2: printf("Dois\n"); break;
    default: printf("Outro\n");
}
```

### Laços de Repetição

```c
// For: quando o número de iterações é conhecido
for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}

// While: enquanto condição for verdadeira
while (x > 0) {
    x--;
}

// Do-While: executa ao menos uma vez
do {
    scanf("%d", &x);
} while (x < 0);
```

---

## Funções

C é organizado em funções. Toda lógica reutilizável deve ser encapsulada em funções:

```c
// Declaração (protótipo)
int soma(int a, int b);

// Definição
int soma(int a, int b) {
    return a + b;
}

int main() {
    int resultado = soma(3, 5);  // Chamada
    printf("Resultado: %d\n", resultado);
    return 0;
}
```

Funções em C passam argumentos **por valor** — a função recebe uma cópia. Para modificar variáveis externas, usa-se **ponteiros**.

---

## Ponteiros e Memória

Este é o coração de C — e o que o diferencia de linguagens modernas.

### O que é um ponteiro?

Um ponteiro é uma variável que armazena o **endereço de memória** de outra variável.

```c
int x = 42;
int *p = &x;     // p aponta para x

printf("%d\n", *p);   // Desreferenciação: imprime 42
*p = 100;             // Modifica x via ponteiro
printf("%d\n", x);    // Imprime 100
```

### Gerenciamento Dinâmico de Memória

```c
#include <stdlib.h>

int *vetor = (int*) malloc(10 * sizeof(int));  // Aloca 10 inteiros

if (vetor == NULL) {
    // Falha na alocação!
    return 1;
}

vetor[0] = 99;

free(vetor);  // OBRIGATÓRIO: libera a memória alocada
```

---

## Arrays e Strings

```c
// Array estático
int numeros[5] = {10, 20, 30, 40, 50};
printf("%d\n", numeros[2]);  // Imprime 30

// String em C = array de char terminado em '\0'
char nome[20] = "Carlos";
printf("Olá, %s!\n", nome);

// Funções úteis de string (string.h)
strlen(nome);          // Comprimento
strcpy(dest, origem);  // Cópia
strcmp(s1, s2);        // Comparação
strcat(s1, s2);        // Concatenação
```

---

## Estrutura

Structs permitem agrupar dados relacionados em uma única estrutura:

```c
typedef struct {
    char nome[50];
    int  idade;
    float salario;
} Funcionario;

Funcionario f1;
strcpy(f1.nome, "Ana");
f1.idade   = 30;
f1.salario = 4500.00;

printf("Nome: %s, Idade: %d\n", f1.nome, f1.idade);
```

Structs são a base para implementar listas ligadas, árvores, filas e outras estruturas de dados em C.

---

## Entrada e Saída

```c
#include <stdio.h>

// Saída formatada
printf("Inteiro: %d | Float: %.2f | String: %s\n", 42, 3.14, "texto");

// Entrada do usuário
int idade;
printf("Digite sua idade: ");
scanf("%d", &idade);   // & = endereço da variável

// Leitura de strings (com espaço)
char linha[100];
fgets(linha, sizeof(linha), stdin);
```

### Arquivos

```c
FILE *arq = fopen("dados.txt", "w");  // Abre para escrita
if (arq != NULL) {
    fprintf(arq, "Linha de texto\n");
    fclose(arq);                       // Sempre fechar!
}
```

---

## Pré-processador

O pré-processador executa antes da compilação:

```c
#define PI 3.14159          // Constante simbólica
#define MAX(a,b) ((a)>(b)?(a):(b))  // Macro com parâmetro

#ifdef DEBUG
    printf("Modo debug ativo\n");
#endif
```

---

## Compilação

### Ciclo de Compilação com GCC

```bash
gcc -Wall -o programa programa.c   # Compilar com avisos
./programa                          # Executar
```

Etapas internas: **Pré-processamento → Compilação → Montagem → Ligação**

### Boas Práticas

- Sempre inicializar variáveis antes de usar
- Verificar retorno de `malloc` (pode ser `NULL`)
- Chamar `free()` para cada `malloc()`
- Usar `const` para valores que não devem mudar
- Dividir o código em múltiplos arquivos `.c` e `.h` para projetos grandes
- Comentar o código de forma clara e objetiva

---

## Referências e Leitura Recomendada

| Recurso | Descrição |
|---|---|
| *The C Programming Language* — Kernighan & Ritchie | O livro original ("K&R"), referência definitiva |
| cppreference.com | Documentação completa da biblioteca padrão |
| `man gcc` | Manual do compilador GCC |
| ISO/IEC 9899 | Padrão oficial da linguagem C |

---


