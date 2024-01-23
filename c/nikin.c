# include <stdio.h>
# include <stdlib.h>
# include "mathutils.h"

int main () {
    struct Point *A;
    struct Point *B;

    A = makepoint(0,-1);
    B = makepoint(-1,0);

    printf("The distance between A and B is %0.6f", distance(A,B));

    return 0;

}
