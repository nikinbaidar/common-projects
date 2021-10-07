
#define isEven(integer) !(integer&1)
#include <stdio.h>

int main() {
    int number;
    printf("Enter an integer ");
    scanf("%d",&number);
    if (isEven(number))
        printf("Even");
    else
        printf("Odd");
   return 0;
}
