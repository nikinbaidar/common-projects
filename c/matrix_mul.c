/* Matrix Multiplication */

#include <stdio.h>
#include <stdlib.h>

int main () {

    system("clear");

    int a[3][3] = {1,0,0,0,1,0,0,0,1} ;
    int b[3][3] = {1,0,0,0,1,0,0,0,1} ;
    int c[3][3];

    int i;
    int j;
    int k;

    int sum;

    for (i = 0 ; i < 3 ; i++)
        for (j = 0 ; j < 3 ; j++) {
            sum = 0;
            for (k = 0 ; k < 3 ; k++) {
                sum += a[i][k]*b[k][j];
            }
            c[i][j] = sum;
        }

    for (i = 0 ; i < 3 ; i++) {
        for (j = 0 ; j < 3 ; j++)
            printf("%d ",c[i][j]);
        printf("\n");
    }


    return 0;
}

/*********************************************************************************/
/* gets or scanf should not be used to take string inputs because these can take */
/* more inputs thatn the array can hold                                          */
/*********************************************************************************/
