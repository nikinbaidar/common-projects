# include <stdio.h>
# include <stdlib.h>

# include "nikin.h"

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
