#include <stdio.h>
int main() {
    if (.1+.2 == .3)
        printf("yes");
    else
        printf("no\n");

    printf("%.16f\n",.1+.2);
    return 0;
}
