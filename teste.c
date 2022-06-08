#include <stdio.h>
#include "stdlib.h"

#define num 2
#define word "salve fml"
#define SOMA(a,b) a+b+5*9

int main()
{
    /* programa do professor bazilio
    testando */
    int a = 2; // a recebe 2
    int x = SOMA(1,2);
    printf("Hello World!, %d\n", x);
    if(a == 2) //Se a == 2 então
        printf("a=2");
    printf("\n%d %s", num, word);
    x = SOMA(3,5);
    return 0;
}