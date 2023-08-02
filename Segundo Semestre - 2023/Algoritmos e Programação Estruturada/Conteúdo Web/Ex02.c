
#include <stdio.h>

int main(int argc, char** argv) {
    
    float nota1, nota2 , media;
    
    printf("Insira a nota1: ");
    scanf("%f", &nota1);
    printf("Insira a nota2: ");
    scanf("%f", &nota2);
    
    media = (nota1 + nota2) / 2;
    
    printf("A média do aluno ficou: %.1f", media);
    
    if (media >= 7) {
        printf("\nALUNO APROVADO !!");
    } else {
        printf("\nALUNO REPROVADO !!");
    }
  
    


    return 0;
}
