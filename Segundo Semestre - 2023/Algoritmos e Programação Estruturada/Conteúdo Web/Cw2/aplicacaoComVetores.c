#include <stdio.h>
int main() {
    
    int numero;
    int i;
    int posicao=0;
    int vetor[10];
    printf("Entre com o numero de ate 3 casas, diferente de zero, a ser procurado em um vetor de 10 posicoes: ");
    scanf("%d", &numero);
    //Preenche o vetor com numeros
    for(i=0;i<10;i++) {
        printf("\nEntre com o numero para a posicao %02d: ", i+1);
        scanf("%d", &vetor[i]);
    }
    //identifica a posicao do numero lido no vetor de entrada
    while(vetor[posicao] != numero) {
        posicao++;
    }
      // Imprime vetor
    for(i=0;i<10;i++) {
        printf("%03d ", vetor[i]);
    }
   // Imprime espaços até) a posição do numero, e em seguida um "*" sob o numero
    printf("\n ");
    for(i=0;i<posicao;i++) {
        printf("    ");
    }
    printf("*");
    return 0;
}