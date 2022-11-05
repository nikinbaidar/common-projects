# include <stdio.h>
# include <stdlib.h>

# include "nikin.h"

void printArr(int *array, int length) 
{  
    printf("{");
    for (int i = 0; i < length; i++)  
        printf("%d, ", *(array+i));  
    printf("\b\b}");
}

int main () {

    struct Point *A;
    struct Point *B;

    double separation;

    system("clear");

    A = makepoint(3,7);
    B = makepoint(5,6);

    separation = distance(A,B);

    printf("%0.6f",separation);

    return 0;

}
