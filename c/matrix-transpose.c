#include <stdio.h>

int main() {
    int A[3][3];
    int B[3][3];
    register int i,j;
    int leading_entry = 1;

    for(i=0;i<3;i++)
        for(j=0;j<3;j++) {
            A[i][j] = leading_entry++;
            B[i][j] = A[i][j];
        }

    for(i=0;i<3;i++) {
        for(j=0;j<3;j++)
            printf(" %d ",A[i][j]);
        printf("\n");
    }

    printf("\n");

    for(i=0;i<3;i++)
        for(j=0;j<3;j++)
            A[i][j] = B[j][i];

    for(i=0;i<3;i++) {
        for(j=0;j<3;j++)
            printf(" %d ",A[i][j]);
        printf("\n");
    }

    return 0;
}
