#include <stdio.h>
main() {

float metragem1 = 0;
float metragem2 = 0;
float resultado = 0;

int resp;

  do {
    printf("C A L C U L O    D E   M E T R O S    Q U A D R A D O S");
    printf("\n \n Digite a primeira metragem do terreno: ");
    scanf("%f",&metragem1);
    printf("\n Digite a segunda metragem do terreno: ");
    scanf("%f",&metragem2);
    resultado = (metragem1 * metragem2);
    printf("\n \n O Terreno tem = %.2f M2 \n",resultado);
    printf("Digite 1 para continuar ou 2 para sair: ");
    scanf("%d", &resp);
  } while (resp==1);

return 0;

}