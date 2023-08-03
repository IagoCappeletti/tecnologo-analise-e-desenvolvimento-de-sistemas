#include <stdio.h>
#include <stdlib.h>

int main() {
    int linha, coluna;
    int matriz[3][3];

    for (linha = 0; linha < 3; linha++) {
        for (coluna = 0; coluna < 3; coluna++) {
            printf("Digite o valor da matriz para a linha %d, coluna %d: ", linha + 1, coluna + 1);
            scanf("%d", &matriz[linha][coluna]);
        }
    }

    printf("\nVeja a sua Matriz:\n");
    for (linha = 0; linha < 3; linha++) {
        for (coluna = 0; coluna < 3; coluna++) {
            printf("%d\t", matriz[linha][coluna]);
        }
        printf("\n");
    }

    system("pause");
    return 0;
}
