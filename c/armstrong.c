#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

int countDigits(int x) {
    int digit_count = 0;

    while (x > 0) {
        x /= 10;
        digit_count++;
    }

    return digit_count;

}

bool isArmstrong(int x) {

    int digits;
    int sum = 0 ;
    int x_copy;

    x_copy = x;

    digits = countDigits(x);

    while (x > 0) {
        sum += pow((x % 10),digits);
        x /= 10;
    }

    return (x_copy == sum);
}

int main () {
    system("clear");

    int lower_limit, upper_limit;
    int i;

    printf("Enter a lower limit: ") ;
    scanf("%d",&lower_limit);

    printf("Enter a uper limit: ") ;
    scanf("%d",&upper_limit);

    for ( i = lower_limit ; i <= upper_limit ; i++ ){
        if (isArmstrong(i))
            printf("%d \n",i);
    }

    return 0;

}
