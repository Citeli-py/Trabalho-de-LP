#include <stdio.h>
#include "stddef.h"

#define num 2
#define word "salve fml"
#define SOMA(a,b) (a+b)

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
    return 0;
}